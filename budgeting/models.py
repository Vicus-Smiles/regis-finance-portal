from django.db import models

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
