# Generated by Django 3.2 on 2022-09-08 22:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('students', '0001_initial'),
        ('curriculum', '0001_initial'),
        ('results', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='result',
            name='student',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='students.studentdetail'),
        ),
        migrations.AddField(
            model_name='result',
            name='subject_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='curriculum.subject'),
        ),
        migrations.AddField(
            model_name='printresult',
            name='exam',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='results.examination'),
        ),
        migrations.AddField(
            model_name='printresult',
            name='student',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='students.studentdetail'),
        ),
        migrations.AddField(
            model_name='examination',
            name='standard_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='curriculum.standard'),
        ),
    ]