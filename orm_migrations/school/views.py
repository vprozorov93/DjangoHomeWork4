from django.views.generic import ListView
from django.shortcuts import render

from .models import Student


def students_list(request):
    template = 'school/students_list.html'
    # students = Student.objects.all().order_by('group')
    queryset = Student.objects.prefetch_related('teachers').order_by('group')

    students = []

    for student in queryset:
        teachers = [{'name': teacher.name, 'subject': teacher.subject} for teacher in student.teachers.all()]
        students.append({'name': student.name, 'group': student.group, 'teachers': teachers})

    context = {'object_list': students}

    return render(request, template, context)
