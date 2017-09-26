# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework import viewsets
from .serializers import *
from .models import *

# Create your views here.
class DogViewSet(viewsets.ModelViewSet):
	serializer_class = DogSerializer
	queryset = Dog.objects.all()

# Create your views here.
class BreedViewSet(viewsets.ModelViewSet):
	serializer_class = BreedSerializer
	queryset = Breed.objects.all()

