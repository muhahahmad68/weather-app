from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.login_page, name='login'),
    path('register', views.register, name='register'),
    path('logout', views.logout_user, name='logout'),
]
