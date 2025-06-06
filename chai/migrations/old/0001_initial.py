# Generated by Django 5.1.5 on 2025-03-30 21:58

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ChaiVariety',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('price', models.IntegerField()),
                ('image', models.ImageField(upload_to='chais/')),
                ('date_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('chai_type', models.CharField(choices=[('PT', 'Plain Tea'), ('MC', 'Masala Chai'), ('GC', 'Ginger Chai'), ('LC', 'Lemon Chai'), ('EC', 'Elaichi Chai'), ('GT', 'Green Tea'), ('BT', 'Black Tea'), ('KC', 'Kulhad Chai')], default='PT', max_length=2)),
                ('description', models.TextField(blank=True, default='')),
            ],
            options={
                'verbose_name': 'Chai Variety',
                'verbose_name_plural': 'Chai Varieties',
            },
        ),
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
                ('address', models.TextField(default='', help_text='Full address of the store')),
                ('phone', models.CharField(blank=True, max_length=15)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('opening_time', models.TimeField(default='09:00', help_text='Store opening time')),
                ('closing_time', models.TimeField(default='21:00', help_text='Store closing time')),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('chai_varieties', models.ManyToManyField(related_name='stores', to='chai.chaivariety')),
            ],
            options={
                'verbose_name': 'Store',
                'verbose_name_plural': 'Stores',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='ChaiReview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], help_text='Rate between 1 and 5')),
                ('comment', models.TextField(blank=True)),
                ('date_added', models.DateTimeField(default=django.utils.timezone.now)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('chai', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='chai.chaivariety')),
            ],
            options={
                'verbose_name': 'Chai Review',
                'verbose_name_plural': 'Chai Reviews',
                'ordering': ['-date_added'],
                'unique_together': {('chai', 'user')},
            },
        ),
    ]
