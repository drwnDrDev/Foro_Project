from django.urls import path
from . import views


urlpatterns = [
    path('threads/', views.threads, name='threads'),
    path('threads/create/', views.threads_create, name='threads_create'),
    path('threads/1',views.threads_show, name='threads_show'),
]