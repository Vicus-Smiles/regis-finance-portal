from django.shortcuts import render, redirect
from .forms import StudentForm
from django.contrib.auth.decorators import login_required

@login_required
def student_register(request):
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('student_register')  # Redirect to a success or same page
    else:
        form = StudentForm()

    return render(request, 'students/student_form.html', {'form': form})

from .models import Student

@login_required
def student_list(request):
    students = Student.objects.all()
    return render(request, 'students/student_list.html', {'students': students})
