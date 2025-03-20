from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib import messages
from .forms import UserUpdateForm, ProfileUpdateForm

# Registration View
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