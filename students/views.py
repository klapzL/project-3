from django.shortcuts import render
from .models import Student

def students_list(request):
    students = Student.objects.all
    context = {
        'students': students
    }
    return render(request, 'students/students_list.html', context)

def student_details(request, student_id):
    students = Student.objects.get(id=student_id)
    context = {
        'student': students
    }
    return render(request, 'students/student_details.html', context)