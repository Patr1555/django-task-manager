from django.urls import path
from .import views

urlpatterns=[path('', views.blog_home, name='blog_home'), #<--path('', ...) → Empty string = base path for the app (/blog/).
             #The name='blog_home' etc. are what you’ll use in templates when linking between pages using {% url 'blog_home' %}
             
             path('update/<int:pk>/', views.blog_update, name='blog_update'),
             path('delete/<int:pk>/', views.blog_delete, name='blog_delete'),
              path('signup/', views.signup_view, name='signup'),
              path('logout/', views.logout_view, name='logout'),
              path('login/', views.login_view, name='login' )

                ]