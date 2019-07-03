from django.contrib import admin
from blogapp.models import Post
from django.db import models
from django.forms import Textarea

# Register your models here.
#
class PostAdmin(admin.ModelAdmin):
    exclude = ['posted']
    prepopulated_fields = {'slug': ('title',)}

    formfield_overrides = {
        models.TextField: {'widget': Textarea( attrs={'rows': 100, 'cols': 160 })},
    }


admin.site.register(Post, PostAdmin)
