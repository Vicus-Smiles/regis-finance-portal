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

class Budget(models.Model):
    category = models.CharField(max_length=50)
    amount_allocated = models.DecimalField(max_digits=12, decimal_places=2)
    fiscal_year = models.IntegerField()

    def __str__(self):
        return f"{self.category} - {self.fiscal_year}"

class Expense(models.Model):
    category = models.CharField(max_length=50)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    date = models.DateField()
    budget = models.ForeignKey(Budget, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.category} - {self.amount}"
    
class Payment(models.Model):
    PAYMENT_TYPES = (
        ('Tuition', 'Tuition'),
        ('Registration', 'Registration Fee'),
        ('Examination', 'Examination Fee'),
    )
    METHOD_CHOICES = (
        ('Cash', 'Cash'),
        ('Mobile Money', 'Mobile Money'),
        ('Bank', 'Bank'),
    )

    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_type = models.CharField(max_length=20, choices=PAYMENT_TYPES)
    method = models.CharField(max_length=20, choices=METHOD_CHOICES)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.student.full_name} - {self.payment_type}"