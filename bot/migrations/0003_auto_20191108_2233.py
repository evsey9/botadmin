# Generated by Django 2.2.6 on 2019-11-08 22:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0002_auto_20191030_1142'),
    ]

    operations = [
        migrations.CreateModel(
            name='Command',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='name')),
                ('description', models.TextField(verbose_name='description')),
                ('no_argument_response', models.CharField(max_length=100, verbose_name='no argument response')),
                ('not_found_response', models.CharField(max_length=100, verbose_name='not found response')),
            ],
            options={
                'verbose_name': 'command',
                'verbose_name_plural': 'commands',
                'db_table': 'commands',
            },
        ),
        migrations.CreateModel(
            name='Day',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='name')),
            ],
            options={
                'verbose_name': 'day of week',
                'verbose_name_plural': 'days of week',
                'db_table': 'daysofweek',
                'ordering': ('id',),
            },
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(blank=True, verbose_name='description')),
                ('date_from', models.DateField(verbose_name='date from')),
                ('date_to', models.DateField(verbose_name='date to')),
            ],
            options={
                'verbose_name': 'event',
                'verbose_name_plural': 'events',
                'db_table': 'events',
            },
        ),
        migrations.CreateModel(
            name='EventType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='name')),
            ],
            options={
                'verbose_name': 'event type',
                'verbose_name_plural': 'event types',
                'db_table': 'event_types',
            },
        ),
        migrations.CreateModel(
            name='GenericAnswer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('input', models.CharField(max_length=50, verbose_name='input')),
                ('output', models.TextField(verbose_name='output')),
            ],
            options={
                'verbose_name': 'generic answer',
                'verbose_name_plural': 'generic answers',
                'db_table': 'genericanswers',
            },
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_start', models.TimeField(verbose_name='time start')),
                ('time_end', models.TimeField(verbose_name='time end')),
                ('name', models.CharField(max_length=50, verbose_name='name')),
                ('description', models.CharField(blank=True, max_length=255, verbose_name='description')),
                ('days', models.ManyToManyField(blank=True, null=True, to='bot.Day', verbose_name='days')),
            ],
            options={
                'verbose_name': 'group',
                'verbose_name_plural': 'groups',
                'db_table': 'groups',
            },
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(max_length=50, verbose_name='country')),
                ('region', models.CharField(max_length=50, verbose_name='region')),
                ('city', models.CharField(max_length=50, verbose_name='city')),
                ('street', models.CharField(max_length=50, verbose_name='street')),
                ('building', models.CharField(max_length=50, verbose_name='building')),
                ('name', models.CharField(max_length=50, verbose_name='name')),
                ('latitude', models.FloatField(verbose_name='latitude')),
                ('longitude', models.FloatField(verbose_name='longitude')),
            ],
            options={
                'verbose_name': 'location',
                'verbose_name_plural': 'locations',
                'db_table': 'locations',
            },
        ),
        migrations.CreateModel(
            name='Signup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_name', models.CharField(max_length=50, verbose_name='last name')),
                ('first_name', models.CharField(max_length=50, verbose_name='first name')),
                ('middle_name', models.CharField(max_length=50, verbose_name='middle name')),
                ('vk_id', models.IntegerField(verbose_name='vk id')),
                ('notes', models.TextField(verbose_name='notes')),
                ('location', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='bot.Location', verbose_name='location')),
            ],
            options={
                'verbose_name': 'signup',
                'verbose_name_plural': 'signups',
                'db_table': 'signups',
            },
        ),
        migrations.CreateModel(
            name='SituationAnswer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('situation', models.CharField(max_length=50, verbose_name='situation')),
                ('output', models.TextField(verbose_name='output')),
            ],
            options={
                'verbose_name': 'situation answer',
                'verbose_name_plural': 'situation answers',
                'db_table': 'situationanswers',
            },
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='name')),
                ('description', models.TextField(verbose_name='description')),
            ],
            options={
                'verbose_name': 'subject',
                'verbose_name_plural': 'subjects',
                'db_table': 'subjects',
            },
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_name', models.CharField(max_length=50, verbose_name='last name')),
                ('first_name', models.CharField(max_length=50, verbose_name='first name')),
                ('middle_name', models.CharField(max_length=50, verbose_name='middle name')),
                ('phone', models.CharField(max_length=20, verbose_name='phone')),
                ('mail', models.CharField(max_length=50, verbose_name='mail')),
                ('age', models.IntegerField(verbose_name='age')),
            ],
            options={
                'verbose_name': 'teacher',
                'verbose_name_plural': 'teachers',
                'db_table': 'teachers',
            },
        ),
        migrations.DeleteModel(
            name='Groups',
        ),
        migrations.DeleteModel(
            name='Locations',
        ),
        migrations.DeleteModel(
            name='Teachers',
        ),
        migrations.AddField(
            model_name='signup',
            name='subject',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='bot.Subject', verbose_name='subject'),
        ),
        migrations.AddField(
            model_name='group',
            name='location',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='bot.Location', verbose_name='location'),
        ),
        migrations.AddField(
            model_name='group',
            name='subject',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='bot.Subject', verbose_name='subject'),
        ),
        migrations.AddField(
            model_name='group',
            name='teacher',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='bot.Teacher', verbose_name='teacher'),
        ),
        migrations.AddField(
            model_name='event',
            name='group',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='bot.Group', verbose_name='group'),
        ),
        migrations.AddField(
            model_name='event',
            name='type',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='bot.EventType', verbose_name='type'),
        ),
    ]
