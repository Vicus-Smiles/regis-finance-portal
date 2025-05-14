from django.shortcuts import render, redirect
from django import forms
from django.db.models import Sum
from .models import Expense
from .forms import ExpenseForm


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
def record_expense(request):
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('record_expense')
    else:
        form = ExpenseForm()

    return render(request, 'budgeting/expense_form.html', {'form': form})


# ------------------------------
# List all expenses + filters + chart
# ------------------------------
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

    return render(request, 'budgeting/expense_list.html', {
        'expenses': expenses,
        'form': form,
        'grouped': grouped
    })

import openpyxl
from django.http import HttpResponse

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
