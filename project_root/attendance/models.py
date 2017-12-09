from django.db import models


from classes.models import ClassModel, RegisterModel
from student.models import StudentModel


STATUS_CHOICES = (
    ('a', 'Attend'),
    ('n', 'Absance'),
    ('l', 'Late'),
)
class DateModel(models.Model):

    #오늘 날짜
    today = models.DateField(verbose_name='오늘 날짜')

    # 오늘 출책 시간
    attend_time = models.TimeField(verbose_name='출책 시간')

    # 학생들 MTM으로 연결
    student = models.ManyToManyField(StudentModel)

    # 과목은 MTO으로 연결
    register = models.ForeignKey(RegisterModel, on_delete=models.CASCADE, verbose_name='과목')

    #출석 정보
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)