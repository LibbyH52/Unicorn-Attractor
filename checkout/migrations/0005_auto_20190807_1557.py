# Generated by Django 2.2.3 on 2019-08-07 14:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0004_order_country'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderlineitem',
            name='feature',
        ),
        migrations.RemoveField(
            model_name='orderlineitem',
            name='order',
        ),
        migrations.DeleteModel(
            name='Order',
        ),
        migrations.DeleteModel(
            name='OrderLineItem',
        ),
    ]
