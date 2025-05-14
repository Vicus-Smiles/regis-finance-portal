from django.shortcuts import render, redirect
from .forms import AcademicHistoryForm

def register_academic_history(request):
    if request.method == 'POST':
        form = AcademicHistoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('register_academic_history')
    else:
        form = AcademicHistoryForm()
    
    return render(request, 'academics/academic_history_form.html', {'form': form})
