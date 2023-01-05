from django.db import models

# Create your models here.
class User (models.Model):
    id = models.AutoField(primary_key = True)
    first_name = models.CharField(max_length = 200)
    last_name = models.CharField(max_length = 200)
    email = models.EmailField()
    password = models.CharField(max_length = 100)