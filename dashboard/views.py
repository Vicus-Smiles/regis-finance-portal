from django.shortcuts import render
from finance.models import Payment
from budgeting.models import Expense
from django.db.models import Sum
from django.contrib.auth.decorators import login_required

@login_required
def dashboard_view(request):
    # Revenue Totals
    total_revenue = Payment.objects.aggregate(Sum('amount'))['amount__sum'] or 0
    tuition_total = Payment.objects.filter(payment_type='Tuition').aggregate(Sum('amount'))['amount__sum'] or 0
    registration_total = Payment.objects.filter(payment_type='Registration').aggregate(Sum('amount'))['amount__sum'] or 0
    exam_total = Payment.objects.filter(payment_type='Examination').aggregate(Sum('amount'))['amount__sum'] or 0

    # Expense Total
    total_expense = Expense.objects.aggregate(Sum('amount'))['amount__sum'] or 0

    context = {
        'total_revenue': total_revenue,
        'tuition_total': tuition_total,
        'registration_total': registration_total,
        'exam_total': exam_total,
        'total_expense': total_expense,  # 👈 pass to template
    }

    return render(request, 'dashboard/dashboard.html', context)
