from django.contrib import admin
from .models import Incidences
from leaflet.admin import LeafletGeoAdmin


# Register your models here.


class IncidencesAdmin(LeafletGeoAdmin):
    list_display = ('name', 'location', 'image')


admin.site.register(Incidences, IncidencesAdmin)