# Generated by Django 3.2.1 on 2021-05-05 13:17

from django.db import migrations
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('chatapp', '0005_session_messages'),
    ]

    operations = [
        migrations.AlterField(
            model_name='session',
            name='messages',
            field=jsonfield.fields.JSONField(),
        ),
    ]