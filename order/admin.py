from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import *
# Register your models here.

class WeightMaterialAdmin(admin.ModelAdmin):
    prepopulated_fields = {"url": ("material","weight",)}
    list_display = ['material','weight',  'url', 'created', 'updated']
    list_display_links = ['material', ]

class TypeMaterialAdmin(admin.ModelAdmin):
    prepopulated_fields = {"url": ("name",)}
    list_display = ['name',  'url', 'created', 'updated']
    list_display_links = ['name', ]

class ContentMaterialAdmin(admin.ModelAdmin):
    prepopulated_fields = {"url": ("name",)}
    list_display = ['name',  'url', 'created', 'updated']
    list_display_links = ['name', ]

class ColorsMaterialAdmin(admin.ModelAdmin):
    prepopulated_fields = {"url": ("name",)}
    list_display = ['name','image_show',  'url', 'created', 'updated']
    list_display_links = ['name', ]

    def image_show(self, obj):
        if obj.photo:
            return mark_safe("<img src='{}' width='60' />".format(obj.photo.url))
        return "None"

    image_show.__name__ = "Картинка"

class ChemicalNameAdmin(admin.ModelAdmin):
    prepopulated_fields = {"url": ("name",)}
    list_display = ['name','image_show', 'chemicalformul', 'varki','url', 'created', 'updated']
    list_display_links = ['name', ]

    def image_show(self, obj):
        if obj.view:
            return mark_safe("<img src='{}' width='60' />".format(obj.view.url))
        return "None"

    image_show.__name__ = "Картинка"

class CountryNameAdmin(admin.ModelAdmin):
    prepopulated_fields = {"url": ("name",)}
    list_display = ['name',  'url', 'created', 'updated']
    list_display_links = ['name', ]

class SewingThreadsAdmin(admin.ModelAdmin):
    prepopulated_fields = {"url": ("gradethread","modelthread")}
    list_display = ['gradethread', 'modelthread','image_show', 'url', 'created', 'updated']
    list_display_links = ['gradethread', ]

    def image_show(self, obj):
        if obj.photo:
            return mark_safe("<img src='{}' width='60' />".format(obj.photo.url))
        return "None"

    image_show.__name__ = "Картинка"

class DecorativeThreadsAdmin(admin.ModelAdmin):
    prepopulated_fields = {"url": ("gradethread","modelthread")}
    list_display = ['gradethread', 'modelthread','image_show', 'url', 'created', 'updated']
    list_display_links = ['gradethread', ]

    def image_show(self, obj):
        if obj.photo:
            return mark_safe("<img src='{}' width='60' />".format(obj.photo.url))
        return "None"

    image_show.__name__ = "Картинка"
#
class DlinaMolniyAdmin(admin.ModelAdmin):
    prepopulated_fields = {"url": ("name",)}
    list_display = ['name', 'status', 'url', 'created', 'updated']
    list_display_links = ['name', ]
#
class MolniyaAdmin(admin.ModelAdmin):
    prepopulated_fields = {"url": ("modelmolniy","colormolniy",)}
    list_display = ['modelmolniy', 'colormolniy','zvena','colorzvena','image_show','status', 'url', 'created', 'updated']
    list_display_links = ['modelmolniy', ]

    def image_show(self, obj):
        if obj.photo:
            return mark_safe("<img src='{}' width='60' />".format(obj.photo.url))
        return "None"

    image_show.__name__ = "Картинка"
#
class KnopokAdmin(admin.ModelAdmin):
    prepopulated_fields = {"url": ("modelknopok","materialknopok","diametrknopok",)}
    list_display = ['modelknopok', 'materialknopok','diametrknopok','colorknopok','image_show','status', 'url', 'created', 'updated']
    list_display_links = ['modelknopok', ]

    def image_show(self, obj):
        if obj.photo:
            return mark_safe("<img src='{}' width='80' />".format(obj.photo.url))
        return "None"

    image_show.__name__ = "Картинка"
#
class ZaklepkaAdmin(admin.ModelAdmin):
    prepopulated_fields = {"url": ("materialzaklepka","diametrzaklepka","colorzaklepka",)}
    list_display = ['materialzaklepka', 'diametrzaklepka','colorzaklepka','image_show','status', 'url', 'created', 'updated']
    list_display_links = ['materialzaklepka', ]

    def image_show(self, obj):
        if obj.photo:
            return mark_safe("<img src='{}' width='80' />".format(obj.photo.url))
        return "None"

    image_show.__name__ = "Картинка"

class CostumerAdmin(admin.ModelAdmin):
    prepopulated_fields = {"url": ("name","organization","email",)}
    list_display = ['name', 'organization','phone','email','status', 'url', 'created', 'updated']
    list_display_links = ['name', ]

class CostumerRecommenAdmin(admin.ModelAdmin):
    prepopulated_fields = {"url": ("costumer","serial_number",)}
    list_display = ['serial_number','costumer', 'status', 'url', 'created', 'updated']
    list_display_links = ['serial_number', ]
    search_fields = ["serial_number", "costumer"]
    list_filter = ( "serial_number","costumer","status")

admin.site.register(WeightMaterial,WeightMaterialAdmin),
admin.site.register(TypeMaterial,TypeMaterialAdmin),
admin.site.register(ContentMaterial,ContentMaterialAdmin),
admin.site.register(ColorsMaterial,ColorsMaterialAdmin),
admin.site.register(ChemicalName,ChemicalNameAdmin),
admin.site.register(CountryName,CountryNameAdmin),
admin.site.register(SewingThreads,SewingThreadsAdmin),
admin.site.register(DecorativeThreads,DecorativeThreadsAdmin),
admin.site.register(DlinaMolniy,DlinaMolniyAdmin),
admin.site.register(Molniya,MolniyaAdmin),
admin.site.register(Knopok,KnopokAdmin),
admin.site.register(Zaklepka,ZaklepkaAdmin),
admin.site.register(Costumer,CostumerAdmin),
admin.site.register(CostumerRecommen,CostumerRecommenAdmin),
