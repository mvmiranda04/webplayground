# Generated by Django 3.2.7 on 2021-12-14 13:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('messenger', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='thread',
            old_name='message',
            new_name='messages',
        ),
    ]
