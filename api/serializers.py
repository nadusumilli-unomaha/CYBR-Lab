from rest_framework import serializers
from .models import *


class DogSerializer(serializers.ModelSerializer):
	class Meta:
		model = Dog
		fields = ('name','age','breed','gender','color','favorite_toy', 'favorite_food')


class BreedSerializer(serializers.ModelSerializer):
	class Meta: 
		model = Breed
		fields = ('name', 'size', 'friendliness', 'trainability', 'shredding_amount', 'exercise_needs')
