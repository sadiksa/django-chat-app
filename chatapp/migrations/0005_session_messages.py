# Generated by Django 3.2.1 on 2021-05-05 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chatapp', '0004_remove_session_messages'),
    ]

    operations = [
        migrations.AddField(
            model_name='session',
            name='messages',
            field=models.TextField(default='messages'),
            preserve_default=False,
        ),
    ]