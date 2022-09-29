# Generated by Django 3.2.13 on 2022-09-28 07:42

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0004_todo_deadline'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todo',
            name='deadline',
        ),
        migrations.AddField(
            model_name='todo',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
