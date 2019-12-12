from django.shortcuts import render
from rest_framework import generics
from .models import User, Recipe, Ingredient, Step
from django.shortcuts import get_object_or_404 #*testing
from rest_framework.response import Response

from .serializers import UserModelSerialzers, RecipeModelSerialzers
# Create your views here.

class ListUsercreate(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserModelSerialzers

class UserRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserModelSerialzers

    # def get_queryset(self):
    #     allRecipes  = Recipe.objects.all()
    #     return allRecipes

    def delete(self, request, *args, **kwargs):
        get_object_or_404(Recipe, pk=kwargs['pk']).delete()
        return Response('Recipe is Deleted')


    