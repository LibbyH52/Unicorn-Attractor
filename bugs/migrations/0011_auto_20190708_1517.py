# Generated by Django 2.2.2 on 2019-07-08 14:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bugs', '0010_auto_20190708_1515'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bug',
            old_name='created_on',
            new_name='posted_on',
        ),
    ]
