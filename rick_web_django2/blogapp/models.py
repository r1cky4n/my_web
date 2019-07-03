"""Rick Web Models."""
from django.db import models
from django.urls import reverse

#================================================
# Blog Models
#================================================

class Post(models.Model):
    """Blog post model."""
    title = models.CharField(max_length=255, unique=True)
    subtitle = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    date = models.DateTimeField(db_index=True, auto_now_add=True)
    body = models.TextField()

    def __str__(self):
        return '%s' % self.title

    def get_absolute_url(self):
        """Get Absolute URL."""
        return reverse("view_blog_post", kwargs={"slug": self.slug})

    def get_date_mdy(self):
        """Get Date in Month, Day, Year format."""
        return self.date.strftime("%B %d, %Y")
