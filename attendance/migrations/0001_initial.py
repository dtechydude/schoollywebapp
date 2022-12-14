# Generated by Django 3.2 on 2022-09-27 00:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('curriculum', '0001_initial'),
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(null=True)),
                ('status', models.BooleanField(default=False)),
                ('attendance_date', models.DateTimeField(auto_now_add=True)),
                ('standard', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='curriculum.standard')),
                ('student_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='students.studentdetail')),
            ],
        ),
    ]
