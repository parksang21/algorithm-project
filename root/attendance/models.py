from django.db import models
from classes.models import ClassModel, RegisterModel
# Create your models here.

STATUS_CHOICES = (
    ('a', 'Attend'),
    ('n', 'Absance'),
    ('l', 'Late'),
)

class AttendModel(models.Model):
    register = models.OneToOneField(RegisterModel)
    date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)

    def __str__(self):
        return self.status