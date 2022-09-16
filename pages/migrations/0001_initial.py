# Generated by Django 3.2 on 2022-09-13 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Admission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=11, null=True)),
                ('middle_name', models.CharField(max_length=11, null=True)),
                ('last_name', models.CharField(max_length=11, null=True)),
                ('dob', models.CharField(max_length=11, null=True)),
                ('gender', models.CharField(max_length=11, null=True)),
                ('phone', models.CharField(max_length=11, null=True)),
                ('email', models.CharField(max_length=11, null=True)),
                ('expected_admission_session', models.CharField(max_length=11, null=True)),
                ('last_class_passed', models.CharField(max_length=11, null=True)),
                ('intended_class', models.CharField(max_length=11, null=True)),
                ('date_submitted', models.CharField(max_length=11, null=True)),
            ],
        ),
    ]
