from django.urls import path
from .views import students_list, student_details

urlpatterns = [
    path('', students_list, name='students_list'),
    path('<int:student_id>', student_details, name='student_details'),
]