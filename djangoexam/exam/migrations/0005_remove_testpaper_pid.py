# Generated by Django 3.2 on 2023-05-21 13:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0004_auto_20230521_2153'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='testpaper',
            name='pid',
        ),
    ]
