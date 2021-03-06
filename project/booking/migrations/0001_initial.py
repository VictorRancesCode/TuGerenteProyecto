# Generated by Django 3.2.5 on 2021-07-27 05:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('bo_nit', models.CharField(blank=True, max_length=20, verbose_name='NIT')),
                ('bo_ci', models.CharField(blank=True, max_length=20, verbose_name='CI')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('description', models.TextField(blank=True)),
                ('price', models.IntegerField(blank=True, help_text='Dia', null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('paid', 'Paid'), ('canceled', 'Canceled')], default='pending', max_length=10)),
                ('check_in', models.DateField()),
                ('check_out', models.DateField()),
                ('payment_type', models.CharField(blank=True, choices=[('cash', 'Cash'), ('cc', 'Credit Card'), ('bank', 'Bank Deposit')], max_length=5, null=True)),
                ('paid_amount', models.IntegerField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bookings', to='booking.customer')),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bookings', to='booking.room')),
            ],
        ),
    ]
