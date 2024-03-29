# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-26 07:48
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Breed',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='', max_length=100)),
                ('size', models.CharField(choices=[('large', 'Large'), ('small', 'Small'), ('tiny', 'Tiny'), ('medium', 'Medium')], max_length=100)),
                ('friendliness', models.IntegerField(validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(1)])),
                ('trainability', models.IntegerField(validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(1)])),
                ('shredding_amount', models.IntegerField(validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(1)])),
                ('exercise_needs', models.IntegerField(validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(1)])),
            ],
        ),
        migrations.CreateModel(
            name='Dog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='', max_length=100)),
                ('age', models.IntegerField(blank=True)),
                ('gender', models.CharField(blank=True, default='', max_length=100)),
                ('color', models.CharField(blank=True, default='', max_length=100)),
                ('favorite_food', models.CharField(blank=True, default='', max_length=100)),
                ('favorite_toy', models.CharField(blank=True, default='', max_length=100)),
                ('breed', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='breed', to='api.Breed')),
            ],
        ),
    ]
