# Generated by Django 4.0.4 on 2022-05-21 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0003_alter_student_school'),
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=18)),
                ('surname', models.CharField(max_length=24)),
                ('birth_date', models.DateField()),
                ('school', models.CharField(max_length=48)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='covers')),
            ],
        ),
    ]
