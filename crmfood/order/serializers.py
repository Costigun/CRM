from .models import Users,Tables,ServicePercentage,Statuses,Meals,MealsToOrder,Meal_Categories,Department,Order,Roles,Check
from rest_framework import serializers
"""
class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ('id','name','surname','roleid','login','email','phone')
"""
class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('__all__')

class MealSerialier(serializers.ModelSerializer):
        class Meta:
            model = Meals
            fields = ('categoryid', 'name', 'description', 'price')

class MealsToOrderSerializer(serializers.ModelSerializer):
    model = MealsToOrder
    fields = ("__all__")

class CheckSerializer(serializers.ModelSerializer):
    class Meta:
        model = Check
        fields = ('id','date','orderid','meals','percentage')


    def to_representation(self, instance):
        result = super().to_representation(instance)

        orderid = instance.orderid
        mealCounts = MealsToOrder.objects.filter(orderid=orderid)
        total_sum = 0
        for cn in mealCounts:
            total_sum +=(cn.quantity * cn.meals.price)

        result['total_sum'] = total_sum
        return total_sum

class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Roles
        fields = ('__all__')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ('email','username')