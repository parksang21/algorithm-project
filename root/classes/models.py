from django.db import models
from django.conf import settings
from student.models import StudentModel

# Create your models here.

class ClassModel(models.Model):
    title = models.CharField(max_length=50, blank = False, verbose_name='강의 제목')
    short_discription = models.CharField(max_length=100, blank=True, null=True, verbose_name='요약 설명')
    class_code = models.CharField(max_length=20, unique=True, blank=False, null=False, verbose_name='학수번호')
    time = models.IntegerField(blank=False, verbose_name='분반')
    prof = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.title + ' ' + self.class_code

class RegisterModel(models.Model):
    class_model = models.ForeignKey(ClassModel, on_delete=models.CASCADE)
    student = models.OneToOneField(StudentModel)