from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.contrib.auth.models import User
from django.http import HttpResponse

import json
import re

from classes.models import RegisterModel
from attendance.models import DateModel

# Create your views here.

@login_required
def today_class(request, id):
    print('%s request the page' % request.user)

    user = get_object_or_404(User, pk=id)
    if(user == request.user):
        print("user is verified")
        class_list = RegisterModel.objects.filter(prof=user)
        print(class_list)
        return render(request, 'classes/class_manage.html', {"class_list":class_list})
    else:
        return render(request, 'error.html', {'err':"unauthorized user"})

@login_required
def class_detail(request, id):
    class_choice = get_object_or_404(RegisterModel, pk=id)
    current_date =  timezone.localtime().strftime('%Y-%m-%d')

    date_list = DateModel.objects.filter(today=current_date, register=class_choice)

    if(request.user == class_choice.prof):
        return render(request, 'classes/class_detail.html',{'class': class_choice,'currenttime':current_date, 'date_model':date_list})
    else:
        return render(request, 'error.html', {'err':"unauthorized user"})


def date_detail(request, c_id, id):
    print('%s---- 수업의 date id[%s]가 넘어왔습니다.' % (c_id, id))
    
    class_choice = get_object_or_404(RegisterModel, id=c_id)
    print("%s ----------- loaded" % class_choice)

    date = get_object_or_404(DateModel, id=id)
    print("%s ----------- loaded" % date)

    student_list = date.studentinstance_set.all()
    

    context = {'date':date, 'students':student_list}
    template = 'classes/date_detail.html'
    return render(request, template, context)


def refresh(request):
    id = request.GET.get('pk', None)
    st_list = request.GET.get('st_list', None)

    p = re.compile(r'\d{10}')
    st_list = p.findall(st_list)

    date = get_object_or_404(DateModel, id=id)
    student_list = date.studentinstance_set.all()

    new_students_name = []
    new_students_time = []
    
    for student in student_list:
        print(student)
        if str(student.student.student_id) not in st_list:
            new_students_name.append(str(student.student.name) + '-' + str(student.student.student_id))
            new_students_time.append(str(student.attend_time))

    context = {'student_name':new_students_name, 'attend_time': new_students_time}
    return HttpResponse(json.dumps(context), content_type="application/json")