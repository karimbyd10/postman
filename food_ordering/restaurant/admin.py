from django.contrib import admin
from .models import Category, Food, Order, OrderItem

class FoodAdmin(admin.ModelAdmin):
    list_display = ('name','price','category','available')

admin.site.register(Category)
admin.site.register(Food, FoodAdmin)
admin.site.register(Order)
admin.site.register(OrderItem)