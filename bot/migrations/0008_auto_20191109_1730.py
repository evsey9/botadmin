# Generated by Django 2.2.6 on 2019-11-09 17:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0007_auto_20191108_2351'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='type',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='bot.EventType', verbose_name='тип'),
        ),
    ]
