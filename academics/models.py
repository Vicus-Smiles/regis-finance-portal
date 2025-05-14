from django.db import models
from students.models import Student

class AcademicHistory(models.Model):
    student = models.OneToOneField(Student, on_delete=models.CASCADE)
    previous_school = models.CharField(max_length=100)
    grade_obtained = models.CharField(max_length=20)
    pre_entry_test = models.BooleanField(default=False)
    orientation_done = models.BooleanField(default=False)
    registration_complete = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.student.full_name} - Academic History"
