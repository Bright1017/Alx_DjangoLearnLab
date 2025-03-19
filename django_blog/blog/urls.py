from django.urls import path
from .views import (
    register,
    profile,
    CustomLoginView,
    CustomLogoutView
)

urlpatterns = [
    # Authentication URLs
    path('register/', register, name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('profile/', profile, name='profile'),

    # Other blog URLs (e.g., post list, detail) go here
]