from django.db import models


# Create your models here.

class Submission(models.Model):
    docfile = models.FileField(upload_to='documents/%Y/%m/%d')
    score = models.DecimalField(default=0.00,max_digits=5,decimal_places=2)
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)
