# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2019-03-27 02:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('aid', models.AutoField(primary_key=True, serialize=False)),
                ('aname', models.CharField(max_length=30)),
                ('age', models.PositiveIntegerField()),
                ('agender', models.CharField(choices=[('0', '男'), ('1', '女')], max_length=1)),
                ('birth_date', models.DateField()),
                ('photo', models.ImageField(default='', upload_to='actors/')),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('mid', models.AutoField(primary_key=True, serialize=False)),
                ('mname', models.CharField(max_length=30)),
                ('m_pub_date', models.DateField()),
                ('mread', models.PositiveIntegerField(default=0)),
                ('mcomment', models.TextField()),
                ('mimage', models.ImageField(upload_to='movies/')),
                ('actors', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stuapp.Actor')),
            ],
        ),
    ]