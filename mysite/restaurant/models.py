from django.db import models
# from django.contrib.auth import User
# Create your models here.
# Models:
# 1. Design the User Model with username(unique field), email(unique field), first_name,
# last_name,m password. (You can use the django inbuilt user model)
# 2. Design A Step Model with step_text(string field, not null), Many to One relationship with
# Recipe
# 3. Design An Ingredient Model with text(not null, string), Many to One relationship with
# Recipe
# 4. Design A Recipe Model with name(string, not null), Foreign Key to User table(one to one
# relationship), One to Many relationship with Step and Ingredient Model
# API:
# You need to create API’s to create a new recipe, get recipes by particular user,
class User(models.Model):
    username = models.CharField(max_length=200,unique= True)
    email = models.EmailField(unique= True)
    firstname = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    password = models.CharField(max_length=200)

    def __str__(self):
        return self.email

class Recipe(models.Model):
    name = models.CharField(max_length=200, null=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='recipeOfOwner')

    def __str__(self):
        return self.name

class Step (models.Model):
    step_text = models.TextField(max_length=200, null=False)
    recipe =  models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='recipeSteps')

    def __str__(self):
        return self.step_text

class  Ingredient(models.Model):
    text = models.TextField(max_length=700)
    recipe =  models.ForeignKey(Recipe, on_delete=models.CASCADE, null=False, related_name='recipeIngredient')

    def __str__(self):
        return self.text




    