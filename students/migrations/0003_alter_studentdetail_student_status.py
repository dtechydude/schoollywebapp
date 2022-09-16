# Generated by Django 3.2 on 2022-09-15 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0002_studentdetail_student_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentdetail',
            name='student_status',
            field=models.CharField(choices=[('active', 'active'), ('graduated', 'graduated'), ('dropped', 'dropped'), ('expelled', 'expelled')], default='active', max_length=15),
        ),
    ]
