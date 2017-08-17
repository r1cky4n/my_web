# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.db.models import permalink

#================================================
# Blog Models
#================================================



class Post(models.Model):
    title = models.CharField(max_length=100, unique=True)          
    slug  = models.SlugField(max_length=100, unique=True)
    date  = models.DateTimeField(db_index=True, auto_now_add=True)
    body  = models.TextField()
    category = models.ForeignKey('blogapp.Category')

    def __unicode__(self):
        return '%s' % self.title

    @permalink
    def get_absolute_url(self):
        return ('view_blog_post', None, {'slug': self.slug})




class Category(models.Model):
    title = models.CharField(max_length=100, unique=True)   # Category Title
    slug  = models.SlugField(max_length=100, unique=True)   # Category Description
    
    def __unicode__(self):
        return '%s' % self.title

    @permalink
    def get_absolute_url(self):
        return ('view_blog_category', None, {'slug': self.slug})



