#connects view to url
from django.urls import path
from .import views

urlpatterns=[
    path('', views.home, name='home'),
    path('update/<int:pk>/', views.updateTask, name='updateTask'),#<int:pk> captures the task’s ID and passes it to your view.
    path('delete/<int:pk>/', views.deleteTask, name='deleteTask'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout')
]
