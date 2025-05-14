from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register_academic_history, name='register_academic_history'),
]
