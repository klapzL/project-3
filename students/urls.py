from django.urls import path
from .views import students_list, student_details, student_create, teachers_list, teacher_create, teacher_details, student_update

urlpatterns = [
    path('students/list/', students_list, name='students_list'),
    path('student/update/<int:student_id>', student_update, name='student_update'),
    path('student/<int:student_id>', student_details, name='student_details'),
    path('student/create/', student_create, name='student_create'),
    path('teachers/list/', teachers_list, name='teachers_list'),
    path('teacher/create/', teacher_create, name='teacher_create'),
    path('teacher/<int:teacher_id>', teacher_details, name='teacher_details'),
]