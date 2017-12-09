from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User

from classes.models import RegisterModel

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
    if(request.user == class_choice.prof):
        return render(request, 'classes/class_manage.html',{})

    else:
        return render(request, 'error.html', {'err':"unauthorized user"})
        