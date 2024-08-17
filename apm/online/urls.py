from django.urls import path
from . import views

urlpatterns = [
    # Path del core
    path('', views.online_classes, name='online-class'),
]
