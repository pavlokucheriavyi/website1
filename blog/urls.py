
from django.urls import path
from . import views


urlpatterns = [
    path('', views.NewsView.as_view(), name='home'),
    path('news/add', views.CreateNewsView.as_view(), name='news_add'),
    path('user/<str:username>', views.UserAllView.as_view(), name='user_news'),
    path('news/<int:pk>', views.NewsDetailView.as_view(), name='news_detail'),
    path('news/<int:pk>/update', views.UpdateNewsView.as_view(), name='news_update'),
    path('news/<int:pk>/delete', views.DeleteNewsView.as_view(), name='news_delete'),
    path('about', views.contacti, name='contacti')


]
