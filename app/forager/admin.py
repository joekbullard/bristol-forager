from django.contrib.gis import admin
from .models import Species, Record, ImageRecord, ImageSpecies


class CustomGeoWidgetAdmin(admin.GISModelAdmin):
    gis_widget_kwargs = {
        "attrs": {
            "default_zoom": 11,
            "default_lon": -2.587910,
            "default_lat": 51.454514,
        },
    }


class ImageRecordInline(admin.TabularInline):
    model = ImageRecord
    extra = 1


class RecordAdmin(CustomGeoWidgetAdmin):
    inlines = [ImageRecordInline]


class ImageSpeciesInline(admin.TabularInline):
    model = ImageSpecies
    extra = 1


class SpeciesAdmin(admin.ModelAdmin):
    inlines = [ImageSpeciesInline]
    extra = 1


admin.site.register(Record, RecordAdmin)
admin.site.register(Species, SpeciesAdmin)
