# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-29 15:24
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=200)),
                ('right_option', models.CharField(max_length=200)),
                ('first_option', models.CharField(max_length=200)),
                ('second_option', models.CharField(max_length=200)),
                ('third_option', models.CharField(max_length=200)),
                ('fourth_option', models.CharField(max_length=200)),
                ('username', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
