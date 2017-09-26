# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Breed(models.Model):
	name = models.CharField(max_length=100, blank=True, default='')
	size_choices = (
		('tiny', 'Tiny'),
		('small', 'Small'),
		('medium', 'Medium'),
		('large','Large'),
	)
	size = models.CharField(max_length=100, choices=size_choices)
	friendliness = models.IntegerField(validators=[
            MaxValueValidator(5),
            MinValueValidator(1)
        ])
	trainability = models.IntegerField(validators=[
            MaxValueValidator(5),
            MinValueValidator(1)
        ])
	shredding_amount = models.IntegerField(validators=[
            MaxValueValidator(5),
            MinValueValidator(1)
        ])
	exercise_needs = models.IntegerField(validators=[
            MaxValueValidator(5),
            MinValueValidator(1)
        ])

class Dog(models.Model):
	name = models.CharField(max_length=100, blank=True, default='')
	age = models.IntegerField( blank=True)
	breed = models.ForeignKey(Breed, related_name='breed', on_delete=models.CASCADE)
	gender = models.CharField(max_length=100, blank=True, default='')
	color = models.CharField(max_length=100, blank=True, default='')
	favorite_food = models.CharField(max_length=100, blank=True, default='')
	favorite_toy = models.CharField(max_length=100, blank=True, default='')
