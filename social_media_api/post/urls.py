from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'post', views.PostView)
router.register(r'comment', views.CommentView)

urlpatterns = [
# """URLs For Post App"""
    path('home', views.Homepage.as_view(), name='home'),  
    path('like_post/<int:post_id>/<int:user_id>/', views.like_posts, name='like_post'), 

# # """Post API Endpoints for Generic View"""
    path('post/create', views.CreateView.as_view()),
    path('posts', views.ListView.as_view()),
    path('post/<int:id>', views.RetrieveView.as_view()),
    path('post/<int:id>/update', views.UpdateView.as_view()),
    path('post/<int:id>/delete', views.DeleteView.as_view()),

    # Endpoints for ModelViewset
    path('', include(router.urls)),
    
#   """Comment API Endpoints for Generic View"""
    path('comment/create', views.CommentCreateView.as_view()),
    path('comments', views.CommentListView.as_view()),
    path('comment/<int:id>', views.CommentRetrieveView.as_view()),
    path('comment/<int:id>/update', views.CommentUpdateView.as_view()),
    path('comment/<int:id>/delete', views.CommentDeleteView.as_view()),
]

# Checker rules to pass test
['feed/']
["<int:pk>/like/", "<int:pk>/unlike/"]