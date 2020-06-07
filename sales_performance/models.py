from django.db import models
from django.contrib.auth.models import User


class Sale(models.Model):
    title = models.CharField(max_length=100)
    desc = models.TextField()
    sale_amount = models.DecimalField(max_digits=20, decimal_places=2)
    sale_date = models.DateTimeField()

    # if user is deleted the sales data for them is also deleted
    sales_person = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        '''Determine how we want this model to print out'''
        return self.title
