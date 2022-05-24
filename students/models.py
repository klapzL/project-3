from django.db import models


class Teacher(models.Model):
    name = models.CharField(max_length=18, null=False)
    surname = models.CharField(max_length=24, null=False)
    birth_date = models.DateField(null=False)
    school = models.CharField(max_length=48, null=False)
    photo = models.ImageField(upload_to='covers', null=True, blank=True)

    def __str__(self):
        return f'{self.name} {self.surname}'


class Student(models.Model):
    name = models.CharField(max_length=18, null=False)
    surname = models.CharField(max_length=24, null=False)
    birth_date = models.DateField(null=False)
    school = models.CharField(max_length=48, null=False)
    grade = models.IntegerField(null=False)
    average_mark = models.DecimalField(decimal_places=2, max_digits=3,null=False)
    photo = models.ImageField(upload_to='covers', null=True, blank=True)
    teacher = models.ForeignKey(Teacher, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} {self.surname}'