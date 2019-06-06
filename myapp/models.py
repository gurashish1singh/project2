# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=32)
    description = models.TextField()

    def __str__(self):
        return self.name
