# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.db import models

# Create your models here.

class medicamentos(models.Model):
    user = models.Foreignkey(settings.AUTH_USER_MODEL)
    Nombre = models.CharField(max_length = 50)
    Gramos = models.CharField(max_length = 50)
    Tabletas = models.CharField(max_length = 50)
    Precio = models.IntegerField()
    created = models.DateTimeField(auto_now = True)
    update = models.DateTimeField(auto_now_add = True)

    def _str_(self):
        return str(self.content)
