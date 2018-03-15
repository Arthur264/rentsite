from django.contrib import admin
from django.contrib.gis.db import models
from mapwidgets.widgets import GooglePointFieldInlineWidget, GooglePointFieldWidget
from models import House, HouseImage, HouseDetails, HouseLocation
from forms import CityForm

# Register your models here.
class HouseMapInline(admin.TabularInline):
    model = HouseLocation
    extra = 1
    can_delete = False
    fields = ('location',)
    formfield_overrides = {
        models.PointField: {"widget": GooglePointFieldInlineWidget}
    }
    
class HouseImageInline(admin.StackedInline):
    model = HouseImage
    can_delete = False
    fk_name = 'house'


class HouseDetailsInline(admin.StackedInline):
    model = HouseDetails
    can_delete = False
    fk_name = 'house'
    
    class Meta:
        verbose_name = 'HouseDetails'
        verbose_name_plural = 'HouseDetails'

class HouseAdmin(admin.ModelAdmin):
    model = House
    inlines = (HouseDetailsInline,HouseMapInline, HouseImageInline)
    fields = ('title', 'discription', 'image_url', 'price', 'bedrooms', 'bathrooms', 'area', 'user')
    # On create field HouseImage not show.
    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(HouseAdmin, self).get_inline_instances(request, obj)
        
    def get_form(self, request, obj=None, **kwargs):
        self.form = CityForm
        return super(HouseAdmin, self).get_form(request, obj, **kwargs)

admin.site.register(House, HouseAdmin)
