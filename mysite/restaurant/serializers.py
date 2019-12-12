from rest_framework import serializers
from .models import User, Recipe, Ingredient, Step
from collections import OrderedDict
# from .models import User, Recipe


class StepModelSerialzers(serializers.ModelSerializer):

    class Meta:
        model = Step
        fields = ['id','step_text']

class IngredientModelSerialzers(serializers.ModelSerializer):

    class Meta:
        model = Ingredient
        fields = ['id','text']


class RecipeModelSerialzers(serializers.ModelSerializer):
    recipeIngredient = IngredientModelSerialzers(many=True)
    recipeSteps = StepModelSerialzers(many=True)

    class Meta:
        model = Recipe
        fields = ['id','name','recipeIngredient','recipeSteps']

class UserModelSerialzers(serializers.ModelSerializer):
    recipeOfOwner = RecipeModelSerialzers(many=True)

    class Meta:
        model = User
        fields =['id', 'username','email', 'firstname','lastname','password','recipeOfOwner']

    def create(self, validated_data):
        recipeOfOwner = validated_data.pop('recipeOfOwner')
        print(recipeOfOwner)
        instance = User.objects.create(**validated_data)
        recipeDict = {}

        for i in range(0,len(recipeOfOwner)):
            if 'name' in recipeOfOwner[i].keys() :
                # Owner
                recipeDict['name'] = str(recipeOfOwner[i]['name'])
                del recipeOfOwner[i]['name']

                recipeInstance =Recipe.objects.create(user=instance,name=recipeDict['name'])
                recipeInstance.save()
               
                # Ingredient
                recipeDict['text'] = recipeOfOwner[i]['recipeIngredient'][0]['text']
                del recipeOfOwner[i]['recipeIngredient']
                print('recipeDict In  recipeIngredient',recipeDict)
                recipeIngredientInstance = Ingredient.objects.create(recipe=recipeInstance,text=recipeDict['text'])
                recipeIngredientInstance.save()

                ##Steps
                recipeDict['step_text']= recipeOfOwner[i]['recipeSteps'][0]['step_text']
                del recipeOfOwner[i]['recipeSteps']
                recipeStepsInstance = Step.objects.create(recipe=recipeInstance, step_text=recipeDict['step_text'])
                recipeStepsInstance.save()

        print(instance)
        return instance

    def update(self, instance, validated_data):
        recipeOfOwner = validated_data.pop('recipeOfOwner')
        instance.username = validated_data.get('username', instance.username)
        instance.lastname = validated_data.get('lastname', instance.lastname)
        instance.password = validated_data.get('password', instance.password)
        instance.save()


        #'recipeOfOwner': [OrderedDict([('name', 'oatmeal'), 
        # ('recipeIngredient', [OrderedDict([('text', 'oats\r\nhot milk or water')])]), 
        # ('recipeSteps', [OrderedDict([('step_text', 'Pour hot water')])])]
        recipeDict = {}
        for i in range(0,len(recipeOfOwner)):
            if 'name' in recipeOfOwner[i].keys() :
                # Owner
                recipeDict['name'] = str(recipeOfOwner[i]['name'])
                del recipeOfOwner[i]['name']
                recipeInstance =Recipe.objects.create(user=instance,name=recipeDict['name'])
                recipeInstance.save()
               
                # Ingredient
                recipeDict['text'] = recipeOfOwner[i]['recipeIngredient'][0]['text']
                del recipeOfOwner[i]['recipeIngredient']
                print('recipeDict In  recipeIngredient',recipeDict)
                recipeIngredientInstance = Ingredient.objects.create(recipe=recipeInstance,text=recipeDict['text'])
                recipeIngredientInstance.save()

                ##Steps
                recipeDict['step_text']= recipeOfOwner[i]['recipeSteps'][0]['step_text']
                del recipeOfOwner[i]['recipeSteps']
                recipeStepsInstance = Step.objects.create(recipe=recipeInstance, step_text=recipeDict['step_text'])
                recipeStepsInstance.save()

        return instance
