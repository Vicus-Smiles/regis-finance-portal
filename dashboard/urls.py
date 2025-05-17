from django.urls import path
from . import views

urlpatterns = [
    path('', views.DashboardView.as_view(), name='dashboard_home'),
    path('analytics/', views.analytics_view, name='dashboard_analytics'),
    path('students/', views.student_list, name='dashboard_student_list'),
    path('students/register/', views.student_register, name='dashboard_student_register'),
    path('expenses/new/', views.record_expense, name='dashboard_record_expense'),
    path('expenses/', views.expense_list, name='dashboard_expense_list'),
    path('expenses/export/', views.export_expenses_to_excel, name='dashboard_export_expenses_excel'),
    path('payments/new', views.record_payment, name='dashboard_record_payment'),
    path('payments/', views.payment_list, name='dashboard_payment_list'),
]