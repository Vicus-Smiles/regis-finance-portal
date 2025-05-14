from django.urls import path
from . import views

urlpatterns = [
    path('record/', views.record_payment, name='record_payment'),
    path('list/', views.payment_list, name='payment_list'),

]
