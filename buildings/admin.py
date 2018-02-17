from django.contrib import admin
from models import House
# Register your models here.
class HouseAdmin(admin.ModelAdmin):
    model = House
    fields = ('title', 'discription', 'image_url', 'price', 'bedrooms', 'bathrooms', 'area', 'user')

admin.site.register(House, HouseAdmin)
# admin.site.register(UserProfile)