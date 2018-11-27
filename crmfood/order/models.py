from django.db import models

from django.contrib.auth.models import AbstractUser

ROLES=[
        ('waiter','WAITER'),
        ('chief','CHIEF'),
        ('admin','ADMIN'),
        ('stripgirl','STRIPTISE'),
    ]

class Profile(models.Model):
    user = models.OneToOneField('Users', on_delete=models.PROTECT)
    roleid = models.ForeignKey('Roles',on_delete=models.CASCADE)
    dateborn = models.DateField()
    phone = models.CharField(max_length=20)

    class Meta:
        verbose_name = 'Profiles'
        verbose_name_plural = 'Профили'

    def __str__(self):
        return self.phone

class Users(AbstractUser):
    name = models.CharField(max_length=50,choices=ROLES,default='waiter')
    #roleid = models.ForeignKey('Roles',on_delete=models.CASCADE)

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Users'
        verbose_name_plural = 'Персонал'


class Roles(models.Model):
    name = models.CharField(max_length=50,choices=ROLES)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Role'
        verbose_name_plural = 'Должность'

class Department(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Department'
        verbose_name_plural = 'Отдел'

class Statuses(models.Model):

    name = models.CharField(max_length=20,default='in progress')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Status'
        verbose_name_plural = 'Статус'

class Tables(models.Model):
    name = models.CharField(max_length=20)

    class Meta:
        verbose_name = 'Tables'
        verbose_name_plural = 'Стол'

class Meal_Categories(models.Model):
    name = models.CharField(max_length=50)
    departmentid = models.ForeignKey(Department,on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Meal Categories'
        verbose_name_plural = 'Блюдо по отделам'

class Meals(models.Model):
    categoryid = models.ForeignKey(Meal_Categories,on_delete=models.CASCADE)
    name = models.CharField(max_length=70)
    description = models.CharField(max_length=150)
    price = models.CharField(max_length=20)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Meal'
        verbose_name_plural = 'Блюдо'

class Order(models.Model):
    waiterid = models.ForeignKey(Users,on_delete=models.CASCADE)
    tableid = models.ForeignKey(Tables,on_delete=models.CASCADE)
    mealsid = models.ForeignKey(Meals,on_delete=models.CASCADE)
    status = models.ForeignKey(Statuses,on_delete=models.CASCADE)
    tablename = models.CharField(max_length=20)

    def __str__(self):
        return self.tablename

    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Заказы'

class MealsToOrder(models.Model):
    quantity = models.CharField(default=1,max_length=20)
    meals = models.ForeignKey(Meals,on_delete=models.CASCADE)
    orderid = models.ForeignKey(Order,on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'ToOrder'
        verbose_name_plural = 'Распределение по заказам'

class ServicePercentage(models.Model):
    percentage = models.IntegerField(default=15)


    class Meta:
        verbose_name = 'Percent'
        verbose_name_plural = 'Проценты'

class Check(models.Model):
    orderid = models.ForeignKey(Order,on_delete=models.CASCADE)
    meals = models.ManyToManyField(Meals)
    date = models.DateTimeField(blank=True,null=True)
    #totalsum = models.DecimalField(max_digits=10,decimal_places=2,default=100,blank=True)
    percentage = models.ForeignKey(ServicePercentage,on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Checks'
        verbose_name_plural = 'Чек'