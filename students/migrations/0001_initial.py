# Generated by Django 4.0.4 on 2022-05-14 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=18)),
                ('surname', models.CharField(max_length=24)),
                ('birth_date', models.DateField()),
                ('school', models.CharField(max_length=16)),
                ('grade', models.IntegerField()),
                ('average_mark', models.DecimalField(decimal_places=2, max_digits=3)),
                ('photo', models.ImageField(null=True, upload_to='covers')),
            ],
        ),
    ]
