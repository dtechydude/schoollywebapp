# Generated by Django 3.2 on 2022-09-27 00:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='PaymentCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='PaymentChart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=150)),
                ('amount_due', models.CharField(blank=True, max_length=150)),
                ('payment_cat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='payment.paymentcategory')),
            ],
        ),
        migrations.CreateModel(
            name='PaymentDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount_paid', models.CharField(blank=True, max_length=150)),
                ('payment_date', models.DateField()),
                ('payment_method', models.CharField(blank=True, choices=[('cash', 'cash'), ('bank_deposit', 'bank_deposit'), ('cheque', 'cheque'), ('pos', 'pos')], max_length=50)),
                ('depositor', models.CharField(blank=True, max_length=150)),
                ('bank_name', models.CharField(blank=True, max_length=150)),
                ('teller', models.CharField(blank=True, max_length=150)),
                ('description', models.CharField(blank=True, max_length=200)),
                ('payment_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='payment.paymentchart')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
