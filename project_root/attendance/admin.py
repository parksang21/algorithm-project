from django.contrib import admin

from .models import DateModel

@admin.register(DateModel)
class DateAdmin(admin.ModelAdmin):
    list_display = ['student_name', 'register', 'today', 'attend_time', 'status']

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.prefetch_related('student')

    def student_name(request, date):
        return '.'.join(student.name for student in date.student.all())