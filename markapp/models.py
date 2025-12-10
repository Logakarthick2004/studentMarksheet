from django.db import models


class marksheet(models.Model):
    name = models.CharField(max_length=50)
    department = models.CharField(max_length=50)
    tamil = models.CharField(max_length=50)
    english = models.CharField(max_length=50)
    python = models.CharField(max_length=50)
    java = models.CharField(max_length=50)
