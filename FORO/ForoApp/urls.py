from django.urls import path
from . import views


urlpatterns = [
    path('profile/<int:user>/', views.profile, name='profile'),    
    path('threads/', views.threads, name='threads'),
    path('threads/create/', views.threads_create, name='threads_create'),
    path('threads/1',views.threads_show, name='threads_show'),
    path('threads/1/reply',views.threads_reply, name='threads_reply'),
]