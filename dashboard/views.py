from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from django import forms
from .models import Expense, Payment
from django.db.models import Sum
from .forms import StudentForm, ExpenseForm, PaymentForm, GuardianForm
import openpyxl
from django.http import HttpResponse



@method_decorator(login_required, name='dispatch')
class DashboardView(TemplateView):
    template_name = 'dashboard/home.html'

@login_required
def student_register(request):
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('student_register')  # Redirect to a success or same page
    else:
        form = StudentForm()

    return render(request, 'dashboard/student_form.html', {'form': form})

from .models import Student

@login_required
def student_list(request):
    students = Student.objects.all()
    return render(request, 'dashboard/student_list.html', {'students': students})


# ------------------------------
# Form for filtering by date
# ------------------------------
class ExpenseFilterForm(forms.Form):
    start_date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}),
        required=False,
        label="Start Date"
    )
    end_date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}),
        required=False,
        label="End Date"
    )


# ------------------------------
# Record a new expense
# ------------------------------

@login_required
def record_expense(request):
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('record_expense')
    else:
        form = ExpenseForm()

    return render(request, 'dashboard/expense_form.html', {'form': form})


# ------------------------------
# List all expenses + filters + chart
# ------------------------------
@login_required
def expense_list(request):
    form = ExpenseFilterForm(request.GET or None)
    expenses = Expense.objects.all().order_by('-date')

    if form.is_valid():
        start = form.cleaned_data.get('start_date')
        end = form.cleaned_data.get('end_date')
        if start:
            expenses = expenses.filter(date__gte=start)
        if end:
            expenses = expenses.filter(date__lte=end)

    # Group by category for the pie chart
    grouped = expenses.values('category').annotate(total=Sum('amount')).order_by('-total')

    return render(request, 'dashboard/expense_list.html', {
        'expenses': expenses,
        'form': form,
        'grouped': grouped
    })


@login_required
def export_expenses_to_excel(request):
    from .models import Expense

    # Create workbook and sheet
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "Expenses"

    # Header row
    ws.append(['Date', 'Category', 'Amount (UGX)', 'Description'])

    # Add all expenses
    for expense in Expense.objects.all().order_by('-date'):
        ws.append([expense.date, expense.category, expense.amount, expense.description])

    # Create response
    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename=expenses.xlsx'
    wb.save(response)
    return response


@login_required
def record_payment(request):
    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('record_payment')  # Or redirect to a success page or list
    else:
        form = PaymentForm()

    return render(request, 'dashboard/payment_form.html', {'form': form})

from .models import Payment

@login_required
def payment_list(request):
    payments = Payment.objects.all().order_by('-date')
    return render(request, 'dashboard/payment_list.html', {'payments': payments})


@login_required
def analytics_view(request):
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

    return render(request, 'dashboard/analytics.html', context)


@login_required
def register_guardian(request):
    if request.method == 'POST':
        form = GuardianForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('register_guardian')
    else:
        form = GuardianForm()
    
    return render(request, 'dashboard/guardian_form.html', {'form': form})