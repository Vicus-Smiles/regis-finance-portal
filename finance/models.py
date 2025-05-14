from django.db import models
from students.models import Student

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
