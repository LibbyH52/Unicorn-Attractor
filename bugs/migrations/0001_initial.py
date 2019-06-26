# Generated by Django 2.2.2 on 2019-06-26 11:14

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bug',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('details', models.TextField()),
                ('posted_on', models.DateField(blank=True, default=django.utils.timezone.now, null=True)),
                ('author', models.CharField(max_length=20)),
                ('views', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(max_length=300)),
                ('posted_on', models.DateField(blank=True, default=django.utils.timezone.now, null=True)),
                ('author', models.CharField(max_length=20)),
                ('bug', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bugs.Bug')),
            ],
        ),
    ]
