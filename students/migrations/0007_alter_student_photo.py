# Generated by Django 3.2 on 2022-06-01 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0006_alter_student_school'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='photo',
            field=models.ImageField(default='', upload_to='covers/'),
        ),
    ]
