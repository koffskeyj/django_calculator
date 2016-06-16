from django.contrib.auth.models import User
from django.db import models
from django.http import request


class Operation(models.Model):
    number1 = models.FloatField()
    number2 = models.FloatField()
    operators = models.CharField(max_length=1)
    result = models.FloatField()
    user = models.ForeignKey(User)
