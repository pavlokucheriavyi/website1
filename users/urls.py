
from django.urls import path
from . import views

urlpatterns = [
    path('reg', views.register, name='registr'),
    path('profile', views.profile, name='profile')
]
