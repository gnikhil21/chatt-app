# Generated by Django 3.1.5 on 2021-07-03 19:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chatroom', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='message',
            old_name='date',
            new_name='time',
        ),
    ]
