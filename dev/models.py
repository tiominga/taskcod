from django.db import models

# Create your models here.
class Dev(models.Model):
    name = models.CharField(max_length=200)
    date_add = models.DateTimeField(auto_now_add=True)

