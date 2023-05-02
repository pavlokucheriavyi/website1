"""website1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("blog.urls")),
    path('', include("users.urls")),
    path('user', views.LoginView.as_view(template_name='users/user.html'), name='user'),
    path('password-reset', views.PasswordResetView.as_view(template_name='users/password_reset.html'), name='password_reset'), #ВОССТАНОВДЛЕНИЕ ПАРОЛЯ
    #страничка на которую перебросит после нажатия батона
    path('password_reset_confirm/<uidb64>/<token>',
        views.PasswordResetConfirmView.as_view(template_name='users/password_reset.html'),
        name='password_reset_confirm'),
    #страничка на которую перебросит юзера после нажатия на ссылку в письме
    path('password_reset_done',
        views.PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'),
        name='password_reset_done'),    
    path('exit', views.LogoutView.as_view(template_name='users/exit.html'), name='exit')
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
