from django.urls import path
from . import views

urlpatterns = [
    # Path del core
    path('', views.face_to_face_classes, name='in-class'),
]
