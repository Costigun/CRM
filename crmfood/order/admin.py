from django.contrib import admin
from .models import Users,Tables,Roles,Statuses,Meals,Meal_Categories,Department,Order,MealsToOrder,Check,ServicePercentage


admin.site.register(Users)
admin.site.register(Tables)
admin.site.register(Roles)
admin.site.register(Statuses)
admin.site.register(Meals)
admin.site.register(Meal_Categories)
admin.site.register(Department)
admin.site.register(Order)
admin.site.register(MealsToOrder)
admin.site.register(Check)
admin.site.register(ServicePercentage)
