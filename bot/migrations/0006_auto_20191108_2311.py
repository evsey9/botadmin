# Generated by Django 2.2.6 on 2019-11-08 23:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0005_auto_20191108_2301'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='group',
            options={'verbose_name': 'group_1', 'verbose_name_plural': 'groups'},
        ),
        migrations.AlterModelOptions(
            name='location',
            options={'verbose_name': 'location_1', 'verbose_name_plural': 'locations'},
        ),
        migrations.AlterModelOptions(
            name='teacher',
            options={'verbose_name': 'teacher_1', 'verbose_name_plural': 'teachers'},
        ),
    ]