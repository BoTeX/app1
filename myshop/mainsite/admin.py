from django.contrib import admin
from .models import Item

# Register your models here.

class ItemAdmin(admin.ModelAdmin):
    # empty_value_display = '-пусто-'
    list_filter = ['pub_date']
    search_fields = ['title']
    list_display = ('title', 'pub_date')
    fieldsets = [
        (None, {'fields': ['title', 'text', 'photo','price' ,'category', 'vip']}),
        ('Personal information', {'fields': ['name', 'number', 'email'], 'classes': ['collapse']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]

admin.site.register(Item, ItemAdmin)