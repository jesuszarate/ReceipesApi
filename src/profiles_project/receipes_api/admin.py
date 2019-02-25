from django.contrib import admin

from . import models

# Register your models here.
admin.site.register(models.UserProfile)
admin.site.register(models.ProfileFeedItem)
admin.site.register(models.Ingredient)
admin.site.register(models.IngredientList)
admin.site.register(models.Instruction)
admin.site.register(models.InstructionList)
admin.site.register(models.Portion)
