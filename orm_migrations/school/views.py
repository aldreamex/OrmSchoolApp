from django.views.generic import ListView
from django.shortcuts import render
from .models import Student


def students_list(request):

    ordering = request.GET.get('ordering', 'group')

    if ordering not in [f.name for f in Student._meta.get_fields()]:
        ordering = 'group'

    students = Student.objects.all().order_by(ordering)

    context = {
        'object_list': students,
        'current_ordering': ordering,
    }

    template = 'school/students_list.html'
    return render(request, template, context)


