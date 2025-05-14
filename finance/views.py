from django.shortcuts import render, redirect
from .forms import PaymentForm

def record_payment(request):
    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('record_payment')  # Or redirect to a success page or list
    else:
        form = PaymentForm()

    return render(request, 'finance/payment_form.html', {'form': form})

from .models import Payment

def payment_list(request):
    payments = Payment.objects.all().order_by('-date')
    return render(request, 'finance/payment_list.html', {'payments': payments})
