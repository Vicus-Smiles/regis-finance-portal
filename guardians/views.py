from django.shortcuts import render, redirect
from .forms import GuardianForm

def register_guardian(request):
    if request.method == 'POST':
        form = GuardianForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('register_guardian')
    else:
        form = GuardianForm()
    
    return render(request, 'guardians/guardian_form.html', {'form': form})
