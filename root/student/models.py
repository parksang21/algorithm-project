from django.db import models
from django.conf import settings

# Create your models here.


class StudentModel(models.Model):
    name = models.CharField(max_length=20)
    student_id = models.IntegerField(unique=True)

    def __str__(self):
        return self.name + '-' + str(self.student_id)