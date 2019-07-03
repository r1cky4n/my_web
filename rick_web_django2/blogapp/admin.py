"""Admin."""
from django.contrib import admin
from django.db import models
from django.forms import Textarea
from blogapp.models import Post

class PostAdmin(admin.ModelAdmin):
    """Admin controls for Posts."""
    exclude = ['posted']
    prepopulated_fields = {'slug': ('title',)}

    formfield_overrides = {
        models.TextField: {'widget': Textarea(attrs={'rows': 100, 'cols': 160})},
    }


admin.site.register(Post, PostAdmin)
