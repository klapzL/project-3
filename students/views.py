from django.shortcuts import render, get_object_or_404
from .models import Student

def students_list(request):
    students = Student.objects.all()
    search_query = request.GET.get('q', '')
    search_query_grade = request.GET.get('grade')
    if search_query:
        students = students.filter(name__contains=search_query)
    if search_query_grade:
        students = students.filter(grade=search_query_grade)
    context = {
        'students': students,
        'search_query': search_query,
    }
    return render(request, 'students/students_list.html', context)

def student_details(request, student_id):
    students = Student.objects.get(id=student_id)
    students = get_object_or_404(Student, pk=student_id)
    context = {
        'student': students
    }
    return render(request, 'students/student_details.html', context)

def student_create(request):
    # form = Student
    context = {

    }
    return render(request, 'students/student_create', context)