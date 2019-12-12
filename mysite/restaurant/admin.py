from django.contrib import admin
from .models import User, Recipe, Step, Ingredient

# Register your models here.

class UserAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)
class RecipeAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)
class StepAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)
class IngredientAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)

admin.site.register(User, UserAdmin)
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Step, StepAdmin)
admin.site.register(Ingredient, IngredientAdmin)



