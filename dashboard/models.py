from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Transaction(models.Model):
    name = models.CharField(max_length=40)
    sum = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(-9_999_999), MaxValueValidator(9_999_999)])
    substraction = models.BooleanField()
    autor = models.CharField(max_length=150)

    class Meta:
        verbose_name = "Транзакция"
        verbose_name_plural = "Транзакции"

    def __str__(self):
        return self.name
