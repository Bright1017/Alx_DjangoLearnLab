from django.urls import path
from .views import (
    post_list,
    register,
    profile,
    CustomLoginView,
    CustomLogoutView
)
from .views import (
    PostListView, PostDetailView,
    PostCreateView, PostUpdateView, PostDeleteView
)


urlpatterns = [
    # Authentication URLs
    path('', post_list, name='post_list'),
    path('register/', register, name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('profile/', profile, name='profile'),
    path('', PostListView.as_view(), name='post_list'),
    "post/<int:pk>/delete/", "post/<int:pk>/update/", "post/new/",
    
    # Create new post
    path('new/', PostCreateView.as_view(), name='post_create'),
    
    # Post detail
    path('<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    
    # Edit post
    path('<int:pk>/edit/', PostUpdateView.as_view(), name='post_update'),
    
    # Delete post
    path('<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),

]
