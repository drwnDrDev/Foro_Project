from django.urls import path
from . import views


urlpatterns = [
    path('threads/', views.threads, name='threads'),
    path('threads/create/', views.threads_create, name='threads_create')
]