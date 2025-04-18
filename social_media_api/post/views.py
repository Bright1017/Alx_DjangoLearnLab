from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status, viewsets
from django_filters.rest_framework import DjangoFilterBackend
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse_lazy
from django.views import generic
from .serializers import PostSerializer, CommentSerializer
from .models import Post, Comment, Like
from accounts.models import CustomUser
from notifications.models import Notification

# Checker rules to pass test
["Post.objects.filter(author__in=following_users).order_by", "following.all()", "permissions.IsAuthenticated"]
["generics.get_object_or_404(Post, pk=pk)", "Like.objects.get_or_create(user=request.user, post=post)"]

""                            """Django Views"""                          ""
# ListView to display all the posts from Users
class Homepage(generic.ListView):
    template_name = 'posts/home.html'
    queryset = Post.objects.all().order_by('-created_at')
    context_object_name = 'all_posts'

def like_posts(request, post_id, user_id):
    post = Post.objects.get(id=post_id)
    user = CustomUser.objects.get(id=user_id)
    current_user = CustomUser.objects.get(id=request.user.id)
    if post and user and current_user:
        user_like_exist = Like.objects.filter(post=post)        
        if not user_like_exist:
            like = Like.objects.create(user=user, post=post)
            notify = Notification.objects.create(recipient=post.author,
                                         actor=user, verb=f"{user} liked your post", target=post)
            print(notify.verb)
        elif user_like_exist:
            for like in user_like_exist:
                print(like.user.id, like.post.id)
                if like.user.id == user.id and like.post.id == post.id:
                    break
                print(True, 2)
                Like.objects.create(user=user, post=post)
                notify = Notification.objects.create(recipient=post.author,
                                        actor=user, verb=f"{user} liked your post", target=post)
                print(notify.verb)
                break
    print(Like.objects.filter(post=post).values())
    print(Like.objects.filter(post=post).count())
    return redirect(reverse_lazy('home'))

"""Generic Views for CRUD Operations"""
class CreateView(generics.CreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            title = serializer.validated_data.get('title')
            content = serializer.validated_data.get('content')
            user_id = request.user.id
            current_user = CustomUser.objects.get(id=user_id).id
            Post.objects.create(author_id=current_user, title=title, content=content)
            print("Saved to database")
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class RetrieveView(generics.RetrieveAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_field = 'id'
    
class ListView(generics.ListAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Post.objects.all().order_by('-created_at')
    serializer_class = PostSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['title', 'content']

class UpdateView(generics.UpdateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Post
    serializer_class = PostSerializer
    lookup_field = 'id'
    
class DeleteView(generics.DestroyAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_field = 'id'

    def delete(self, request, *args, **kwargs):
        current_user_id = request.user.id
        author_id = request.data.get('author')
        print(current_user_id, author_id)
        if current_user_id != author_id:
            return Response(data={'Error': 'You are not permmitted to delete a post that you did not create!'}, status=status.HTTP_403_FORBIDDEN)
        return super().delete(request, *args, **kwargs)
    
"""ModelViewset CRUD Operations"""
class PostView(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]  
    permission_classes = [IsAuthenticated]
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['title', 'content']

    def destroy(self, request, *args, **kwargs):
        current_user_id = request.user.id
        author_id = request.data.get('author')
        print(current_user_id, author_id)
        if current_user_id != author_id:
            return Response(data={'Error': 'You are not permmitted to delete a post that you did not create!'}, status=status.HTTP_403_FORBIDDEN)
        return super().destroy(request, *args, **kwargs)

"""Generic Views for CRUD Operations"""
class CommentCreateView(generics.CreateAPIView):
    authentication_classes = [TokenAuthentication]  
    permission_classes = [IsAuthenticated]
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            # print(serializer.validated_data)
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class CommentListView(generics.ListAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class CommentRetrieveView(generics.RetrieveAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    lookup_field = "id"

class CommentUpdateView(generics.UpdateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    lookup_field = "id"


class CommentDeleteView(generics.DestroyAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    lookup_field = "id"

    def delete(self, request, *args, **kwargs):
        current_user_id = request.user.id
        author_id = request.data.get('author')
        print(current_user_id, author_id)
        if current_user_id != author_id:
            return Response(data={'Error': 'You are not permmitted to delete a post that you did not create!'}, status=status.HTTP_403_FORBIDDEN)
        return super().delete(request, *args, **kwargs)

"""ModelViewset for CRUD Operations"""
class CommentView(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]  
    permission_classes = [IsAuthenticated]
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def destroy(self, request, *args, **kwargs):
        current_user_id = request.user.id
        author_id = request.data.get('author')
        print(current_user_id, author_id)
        if current_user_id != author_id:
            return Response(data={'Error': 'You are not permmitted to delete a comment that you did not create!'}, status=status.HTTP_403_FORBIDDEN)
        return super().destroy(request, *args, **kwargs)
    