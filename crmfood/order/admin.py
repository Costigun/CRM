from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserChangeForm,CustomUserCreationForm
from .models import Users,Tables,Roles,Statuses,Meals,Meal_Categories,Department,Order,MealsToOrder,Check,ServicePercentage,Profile

class UserInLine(admin.StackedInline):
    model = Profile
    extra = 0


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = Users
    list_display = ('email','name')
    inlines = [UserInLine]

admin.site.register(Users,CustomUserAdmin)
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
