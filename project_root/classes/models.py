from django.db import models
from django.conf import settings
from student.models import StudentModel

import datetime

# Create your models here.

class ClassModel(models.Model):

    # 강좌명
    title = models.CharField(max_length=50, blank = False, verbose_name='강의 제목')

    # 요약 설명
    short_discription = models.CharField(max_length=100, blank=True, null=True, verbose_name='요약 설명')

    # 학수번호
    class_code = models.CharField(max_length=20, unique=True, blank=False, null=False, verbose_name='학수번호')

    # 시수
    credit = models.IntegerField(default=3, verbose_name='시수')

    # 전공
    major = models.CharField(max_length=20, verbose_name='전공')

    def __str__(self):
        return self.title + ' - ' + self.class_code

class RegisterModel(models.Model):

    # 교수자
    prof = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='교수자')

    # 수업
    class_model = models.ForeignKey(ClassModel, on_delete=models.CASCADE, verbose_name='과목')

    # 분반
    division = models.IntegerField(default = 1, blank=False, null=False, verbose_name='분반')

    # 학생 등록
    student = models.ManyToManyField(StudentModel)

    # 요일1
    # validator 필요함
    day = models.CharField( max_length=20, default='mon', verbose_name="요일 및 시간")

    def __str__(self):
        return self.class_model.title + "(" + self.class_model.class_code + '-' + str(self.division) + ')'
