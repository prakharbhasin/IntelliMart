from django.contrib import admin
from .models import *


# Register your models here.
'''
Configure Admin Side Views for each model:

This controls how they appear on the admin view panel

'''
class AdminStore(admin.ModelAdmin):
    list_display = ['id', 'name', 'description', 'address', 'owner']

class AdminProduct(admin.ModelAdmin):
    list_display = ['id', 'name', 'price', 'quantity', 'category', 'store']

class AdminCategory(admin.ModelAdmin):
    list_display = ['id', 'name']

class AdminCustomer(admin.ModelAdmin):
    list_display = ['id', 'name', 'email']

class AdminOwner(admin.ModelAdmin):
    list_display = ['id', 'name', 'email']

class AdminCartProduct(admin.ModelAdmin):
    list_display = ['id', 'user', 'product', 'quantity', 'ordered']

class AdminSlot(admin.ModelAdmin):
    list_display = ['id', 'start_hour', 'end_hour', 'store', 'total_people']


''' MODEL REGISTRATION '''
admin.site.register(Product, AdminProduct)
admin.site.register(Category, AdminCategory)
admin.site.register(Customer, AdminCustomer)
admin.site.register(Store, AdminStore)
admin.site.register(Owner, AdminOwner)
admin.site.register(CartProduct, AdminCartProduct)
admin.site.register(Slot, AdminSlot)