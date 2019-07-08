# Generated by Django 2.2.2 on 2019-07-08 14:38

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('bugs', '0011_auto_20190708_1517'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bug',
            name='posted_on',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True),
        ),
        migrations.AlterField(
            model_name='comment',
            name='created_on',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True),
        ),
    ]
