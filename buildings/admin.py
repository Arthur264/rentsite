from django.contrib import admin
from django.contrib.gis.db import models
# from mapwidgets.widgets import GooglePointFieldInlineWidget, GooglePointFieldWidget
from models import House, HouseImage, HouseDetails


# Register your models here.

class HouseImageInline(admin.StackedInline):
    model = HouseImage
    can_delete = False
    fk_name = 'house'


class HouseDetailsInline(admin.StackedInline):
    model = HouseDetails
    can_delete = False
    fk_name = 'house'

class HouseAdmin(admin.ModelAdmin):
    model = House
    inlines = (HouseDetailsInline, HouseImageInline)
    fields = ('title', 'discription', 'image_url', 'price', 'bedrooms', 'bathrooms', 'area', 'user')
    # formfield_overrides = {
    #     models.PointField: {"widget": GooglePointFieldWidget}
    # }

    # On create field HouseImage not show.
    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(HouseAdmin, self).get_inline_instances(request, obj)


admin.site.register(House, HouseAdmin)
