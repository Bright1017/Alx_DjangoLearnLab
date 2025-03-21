from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib import messages
from .forms import UserUpdateForm, ProfileUpdateForm
from django.views.generic import (
    ListView, DetailView, 
    CreateView, UpdateView, DeleteView
)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Post
from .forms import PostForm


# Registration View
def post_list(request):
    return render(request, 'blog/post_list.html')

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log the user in after registration
            return redirect('post_list')  # Redirect to blog homepage
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

# Custom Login View (using Django's built-in)
class CustomLoginView(LoginView):
    template_name = 'registration/login.html'

# Custom Logout View
class CustomLogoutView(LogoutView):
    next_page = 'post_list'  # Redirect to homepage after logout

# Profile Management View
# @login_required
# def profile(request):
#     if request.method == 'POST':
#         # Update user info (example: email)
#         user = request.user
#         user.email = request.POST.get('email')
#         user.save()
#         return redirect('profile')
#     return render(request, 'registration/profile.html')


@login_required
def profile(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(
            request.POST,
            request.FILES,
            instance=request.user.profile
        )

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your profile has been updated!')
        return redirect('profile')
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'user_form': user_form,
        'profile_form': profile_form
    }
    return render(request, 'registration/profile.html', context)

class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'
    ordering = ['published_date']
    paginate_by = 5

class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html'

    def form_valid(self, form):
        # Automatically set the author to current user
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    login_url = '/login/'  # Redirect if not authenticated
    redirect_field_name = 'next'

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html'

    def get_queryset(self):
        # Only allow authors to edit their own posts
        return super().get_queryset().filter(author=self.request.user)

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author
    
    def handle_no_permission(self):
        return redirect('post_list')
    
        # Add queryset filtering
    def get_queryset(self):
        return super().get_queryset().filter(author=self.request.user)
    
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'blog/post_confirm_delete.html'
    success_url = '/posts/'

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author
    
    def handle_no_permission(self):
        return redirect('post_list')
    
       # Add queryset filtering
    def get_queryset(self):
        return super().get_queryset().filter(author=self.request.user)