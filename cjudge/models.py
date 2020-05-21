from django.db import models


# Create your models here.

class Submission(models.Model):
    docfile = models.FileField(upload_to='documents/%Y/%m/%d')
    created = models.DateTimeField(auto_now=True)
