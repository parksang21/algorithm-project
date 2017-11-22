from django.shortcuts import render

# Create your views here.


def attendance_check(request):
    return render(request, 'attendance/attend.html', {})
    