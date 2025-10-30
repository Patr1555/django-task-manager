"""
URL configuration for mytask project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.shortcuts import redirect


urlpatterns = [
    path('', lambda request: redirect('blog_home')),

    path('admin/', admin.site.urls),
    
    #path('', include('task.urls')),
    path('blog/',include('blog.urls')),#include('blog.urls') → tells Django to look inside your blog app for its own URL patterns.
]## your new Blog app routes^


#here you connect the urls from the app urls.py, to this main project urls.py^^.