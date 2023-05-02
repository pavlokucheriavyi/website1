from django.shortcuts import render, redirect
# from django.contrib.auth.forms import UserCreationForm
from .form import RegisterForm, UserUpdateForm, UserImageForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Пользователь {username} был успешно создан')
            return redirect('home')
    else:
        form = RegisterForm()
    return render(request, 'users/registration.html',
                  {
                      'title': "Страница регистрации",
                      'form': form
                  }
                  )


@login_required
def profile(request):
    if request.method == "POST":
        profileImageForm = UserImageForm(request.POST, request.FILES, instance=request.user.profile)
        profileUpdateForm = UserUpdateForm(request.POST, instance=request.user)

        if profileImageForm.is_valid() and profileUpdateForm.is_valid():
            profileImageForm.save()
            profileUpdateForm.save()
            username = profileUpdateForm.cleaned_data.get('username')
            messages.success(request, f'Данные пользователя {username} были успешно обновлёны')
            return redirect('profile')

    profileImageForm = UserImageForm(instance=request.user.profile)
    profileUpdateForm = UserUpdateForm(instance=request.user)

    data = {
        'profileImageForm': profileImageForm,
        'profileUpdateForm': profileUpdateForm
    }

    return render(request, 'users/profile.html', data)
