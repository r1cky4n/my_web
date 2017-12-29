# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.db.models import permalink
from datetime import datetime

#================================================
# Blog Models
#================================================

class Post(models.Model):
    title    = models.CharField(max_length=255, unique=True)          
    subtitle = models.CharField(max_length=255)          
    slug     = models.SlugField(max_length=255, unique=True)
    date     = models.DateTimeField(db_index=True, auto_now_add=True)
    body     = models.TextField()

    def __unicode__(self):
        return '%s' % self.title

    @permalink
    def get_absolute_url(self):
        return ('view_blog_post', None, {'slug': self.slug})

    def get_date_MDY(self):
        return self.date.strftime("%B %d, %Y")
        



