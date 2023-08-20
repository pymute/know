from django.db import models
from django.contrib.auth.models import User,AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    CHOICES = (
        ('admin',1),
        ('user',2)
    )
    roles = models.PositiveSmallIntegerField(default=1,choices=CHOICES)
class DataModel(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    age = models.IntegerField()
    phone_number = models.CharField(max_length=13,default='')

    def __str__(self):
        return self.surname

    class Meta:
        db_table = 'okey'
