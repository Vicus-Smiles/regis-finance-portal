from django.urls import path
from . import views

urlpatterns = [
    path('record/', views.record_expense, name='record_expense'),
    path('list/', views.expense_list, name='expense_list'),
    path('export/excel/', views.export_expenses_to_excel, name='export_expenses_excel'),
]
