from django.contrib import admin

from .models import Category, Room, Plant

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_filter = ['name']
    search_fields = ['name']
    ordering = ['name']    
    list_select_related = True

class RoomAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'exposure',
        'temperature',
        'humidity',
        'draft',
        ]
    list_filter = [
        'name',
        'exposure',
        'temperature',
        'humidity',
        'draft',
        ]
    search_fields = ['name']
    ordering = [
        'name',
        'exposure',
        'temperature',
        'humidity',
        'draft',
        ]
    list_select_related = True

class PlantAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'watering_interval',
        'fertilizing_interval',
        'required_exposure',
        'required_temperature',
        'required_humidity',
        'blooming',
        'difficulty',
        'last_watered',
        'last_fertilized',
        ]
    list_filter = [
        'name',
        'watering_interval',
        'fertilizing_interval',
        'required_exposure',
        'required_temperature',
        'required_humidity',
        'blooming',
        'difficulty',
        'last_watered',
        'last_fertilized',
        ]
    ordering = [
        'name',
        'watering_interval',
        'fertilizing_interval',
        'required_exposure',
        'required_temperature',
        'required_humidity',
        'blooming',
        'difficulty',
        'last_watered',
        'last_fertilized',
        ]
    search_fields = ['name']
    autocomplete_fields = ['category', 'room']
    list_select_related = True

admin.site.register(Category, CategoryAdmin)
admin.site.register(Room, RoomAdmin)
admin.site.register(Plant, PlantAdmin)

