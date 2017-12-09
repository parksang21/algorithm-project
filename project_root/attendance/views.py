from django.shortcuts import render, redirect, get_object_or_404

# import DBs
from student.models import StudentModel
from classes.models import RegisterModel
from attendance.models import DateModel

# Create your views here.

#attend/{{class_id}}/load/ url redirecting
def detour(request, class_hash):
    return render(request, 'attendance/temp_first.html',{'class_hash':class_hash})

# attend/check url POST 요청 처리, GET 방식으로 들어오는 것은 거부
def checkattend(request):
    if request.method == 'POST':

        print('\n\nSuccess redirecting....\nFirst authentication is done\n')

        class_hash = request.POST['class_hash']
        print('hash input ---------- %s' % class_hash)

        class_info = get_object_or_404(RegisterModel, class_hash=class_hash)
        print('[Success] ----------- %s  /  pk : %s' % (class_info, class_info.pk))

        return render(request, 'attendance/test.html', {'class_pk':class_info.pk})
    
    return render(request, 'attendance/error.html', {})


# attend/success url POST 요청처리, GET 방식으로 들어오는 것은 거부
def success(request):
    if request.method == 'POST':
        print('\n\nThird authentication is done\n')

        # 학생 정보 받기
        student_id = request.POST['student_id'] or 0
        print('student_id [%s] ---------- attemps to attend' % student_id)

        # 학생 정보와 매칭되는 학생 Data 찾기
        student_info = get_object_or_404(StudentModel, student_id=student_id)
        print('[Success] ---------- [%s]' % student_info)

        # 수업 정보 만들기
        class_pk = request.POST['class_pk']
        class_info = get_object_or_404(RegisterModel, pk=class_pk)
        print('[Success] ---------- [%s]' % class_info)

        # 등록한 학생인지 검사
        if (student_info in class_info.student.all()):
            print('Register Conformed')

            # --------------- 이 부분에 출석 Data 형성하는 코드를 넣으면 된다.
            new_attend = DateModel()
            # ------------------------------------------------------------

            return render(request, 'attendance/success.html', {"student" : student_info})
        else:
            print('student [%s] has not registered [%s]' %(student_info, class_info))
            err_message = '해당 과목 수강자가 아닙니다.'
    else:
        print('잘못된 경로로 접근하였습니다.')
        err_message = '인증 실패'

    return render(request, 'attendance/error.html', {'err' : err_message})