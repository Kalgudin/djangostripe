from django.contrib import admin

from payments.models import Items, Order


@admin.register(Items)
class ItemsAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'price', 'description']
    search_fields = ('name', 'description')


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    pass



