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
            name='Examination',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=150)),
                ('standard_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='curriculum.standard')),
            ],
        ),
        migrations.CreateModel(
            name='Session',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exam_date', models.DateField(null=True)),
                ('cand_score', models.IntegerField(blank=True)),
                ('pass_mark', models.IntegerField(blank=True)),
                ('remark', models.CharField(blank=True, max_length=150)),
                ('file', models.FileField(blank=True, upload_to='result')),
                ('exam', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='results.examination')),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='results.session')),
                ('standard', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='curriculum.standard')),
                ('student', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='students.studentdetail')),
                ('subject_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='curriculum.subject')),
            ],
        ),
        migrations.CreateModel(
            name='PrintResult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exam_year', models.DateField(null=True)),
                ('file', models.FileField(blank=True, upload_to='result')),
                ('exam', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='results.examination')),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='results.session')),
                ('student', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='students.studentdetail')),
            ],
        ),
    ]
