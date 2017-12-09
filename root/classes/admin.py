from django.contrib import admin
from .models import ClassModel,RegisterModel
# Register your models here.


@admin.register(ClassModel)
class ClassAdmin(admin.ModelAdmin):
    # list_display = ['title', 'class_code', 'time', 'prof']
    pass

@admin.register(RegisterModel)
class RegisterAdmin(admin.ModelAdmin):
    # list_distplay = ['class_model', 'student', 'register_date']
    pass