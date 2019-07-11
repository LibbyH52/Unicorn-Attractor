# Generated by Django 2.2.2 on 2019-07-11 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bugs', '0012_auto_20190708_1538'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bug',
            name='fix_status',
            field=models.CharField(choices=[('Done', 'Done'), ('Doing', 'Doing'), ('ToDo', 'ToDo')], default='ToDo', max_length=6),
        ),
    ]
