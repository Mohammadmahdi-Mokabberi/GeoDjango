from __future__ import unicode_literals
import uuid
from django.db.models import Manager as GeoManager
from django.contrib.gis.db import models
import folium
import io
from PIL import Image


class Incidences(models.Model):
    name = models.CharField(max_length=32, unique=True)
    location = models.PointField(srid=4326)
    image = models.ImageField(upload_to="images", blank = True)
    objects = GeoManager()

    def __unicode__(self):
        return self.name
    
    def get_location_x (self):
        list = str(self.location).split(';')[1]
        list = list.split('(')[1]
        list = list.split(')')[0]
        list = list.split(' ')
        x = list[0]
        return x
    
    def get_location_y(self):
        list = str(self.location).split(';')[1]
        list = list.split('(')[1]
        list = list.split(')')[0]
        list = list.split(' ')
        y = list[1]
        return y

    def location_to_image(self, x, y):
        name = 'media/image/' + uuid.uuid4().hex[:5] + '.png'
        map_obj = folium.Map([x, y], zoom_start=13, control_scale=True)
        img = Image.open(io.BytesIO(map_obj._to_png()))
        img.save(name)
        return name

    def save(self, *args, **kwargs):
        y = self.get_location_x()
        x = self.get_location_y()
        self.image = self.location_to_image(x, y)
        super(Incidences, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = "Incidences"