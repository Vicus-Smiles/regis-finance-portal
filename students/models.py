from django.db import models

class Student(models.Model):
    student_id = models.CharField(max_length=20, unique=True)
    full_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=10)
    date_of_birth = models.DateField()
    passport_photo = models.ImageField(upload_to='student_photos/')
    village = models.CharField(max_length=50)
    parish = models.CharField(max_length=50)
    subcounty = models.CharField(max_length=50)
    district = models.CharField(max_length=50)

    def __str__(self):
        return self.full_name
