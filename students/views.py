from django.shortcuts import render, get_object_or_404, redirect
from .models import Student, Teacher
from .forms import StudentForm, TeacherForm


def students_list(request):
    search_query_grade = request.GET.get('grade')
    search_query_name = request.GET.get('q', '')
    teacher_search = request.GET.get('t', '')
    students = Student.objects.all()
    teachers_non_repeated = [t for t in Teacher.objects.all()]
    if teacher_search:
        teacher = Teacher.objects.get(teacher_search)
        students = Student.objects.filter(teacher=teacher)
    if search_query_name:
        students = students.filter(name__contains=search_query_name)
    if search_query_grade:
        students = students.filter(grade=search_query_grade)
    context = {
        'students': students,
        'search_query': search_query_name,
        'teacher_search': teacher_search,
        'teachers_list': teachers_non_repeated
    }
    return render(request, 'students/students_list.html', context)


def students_by_teachers(request, teacher_id):
    teacher = Teacher.objects.get(id=teacher_id)
    student = Student.objects.filter(teacher=teacher)

def teachers_list(request):
    teachers = Teacher.objects.all()
    search_query = request.GET.get('q', '')
    if search_query:
        teachers = teachers.filter(name__contains=search_query)
    context = {
        'teachers': teachers,
        'search_query': search_query,
    }
    return render(request, 'students/teachers_list.html', context)


def student_details(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    context = {
        'student': student
    }
    return render(request, 'students/student_details.html', context)


def student_create(request):
    # form = StudentForm()
    form = StudentForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid:
            form.save()
            return redirect('students_list')
    context = {
        'form': form
    }
    return render(request, 'students/student_create.html', context)


def teacher_create(request):
    form = TeacherForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid:
            form.save()
            return redirect('teachers_list')
    context = {
        'form': form
    }
    return render(request, 'students/teacher_create.html', context)


def teacher_details(request, teacher_id):
    teacher = get_object_or_404(Teacher, pk=teacher_id)
    context = {
        'teacher': teacher
    }
    return render(request, 'students/teacher_details.html', context)


def student_update(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    form = StudentForm(request.POST or None, instance=student)
    if request.method == 'POST':
        if form.is_valid:
            form.save()
            return redirect('students_list')
    context = {
        'form': form
    }
    return render(request, 'students/student_update.html', context)


def student_delete(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    if request.method == 'POST':
        student.delete()
        return redirect('students_list')
    context = {
        'student': student
    }
    return render(request, 'students/student_delete.html', context)