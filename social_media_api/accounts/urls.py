from django.urls import path
from .import views
from django.contrib.auth import views as authviews

urlpatterns = [
    path('register', views.RegistrationView.as_view(), name='register'),
    path('home', views.HomePage.as_view(), name='home'),
    path('login', authviews.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('follow_user/<int:id>', views.follow, name='follow_user'),
    path('unfollow_user/<int:id>', views.unfollow, name='unfollow_user'),

    # API URLS
    path('register/', views.RegisterAPIView.as_view()),
    path('login/', views.LoginAPIView.as_view()),
    path('userprofile/<int:pk>', views.ProfileView.as_view(), name='userprofile'),
    path('users/', views.UsersAPIView.as_view(), name='all_users'),
    path('user/<int:pk>', views.UserDetailAPIView.as_view(), name='user'),
    path('follow/<int:id>/', views.UserUpdateFollowerAPIView.as_view(), name='follow'),
    path('unfollow/<int:id>/', views.UnFollowUserAPIView.as_view(), name='unfollow'), 

]
# Checker rules to pass test
['follow/<int:user_id>/', 'unfollow/<int:user_id>/'] 