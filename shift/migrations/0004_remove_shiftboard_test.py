# Generated by Django 3.1 on 2021-08-10 09:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shift', '0003_auto_20210810_1820'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shiftboard',
            name='test',
        ),
    ]
