"""
URL configuration for FORO project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path
from categories.views import categories
from home.views import *
from users.views import *
from votes.views import *
from threads.views import *
from tags.views import *
from django.contrib.auth.views import LoginView, LogoutView
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', home),
    path('contact', contact),
    path('about', about),
    path('admin/', admin.site.urls),
    path('categories/', categories),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('votes/', votes, name='vote'),
    path('tags/', tags, name='tags'),
  
    path('threads/', threads, name='threads'),
    path('thread/<int:id>/', thread, name='thread'),


]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
