from django.db import models

class OracleInstance(models.Model):
    name = models.CharField(max_length=100)
    dsn = models.CharField(max_length=255)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
