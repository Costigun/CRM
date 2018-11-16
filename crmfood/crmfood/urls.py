"""crmfood URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import include,url
from rest_framework import routers
from order import views

#router = routers.DefaultRouter()
#router.register(r'users', views.UsersView)

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'reg/v1/',include('reg.urls')),
    #url(r'',include(router.urls)),
    #url(r'users',views.UsersView.as_view()),
    url(r'order',views.OrderView.as_view()),
    url(r'checks',views.CheckView.as_view()),
    url(r'meals',views.MealView.as_view()),
    url(r'MealsToOrder',views.MealsToOrderView.as_view()),
    url(r'^api-auth/', include('rest_framework.urls')),
]
