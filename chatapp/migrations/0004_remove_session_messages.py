# Generated by Django 3.2.1 on 2021-05-05 10:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chatapp', '0003_session_messages'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='session',
            name='messages',
        ),
    ]
