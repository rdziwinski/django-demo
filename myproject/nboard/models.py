from django.db import models
from django.contrib.auth.models import User


STATUS = (
    (0, "Future"),
    (1, "In Progress"),
    (2, "Archive")
)

TYPE = (
    (0, "Announcement"),
    (1, "Maintenance"),
    (2, "Problem")
)


class Notice(models.Model):
    title = models.CharField(max_length=64)
    slug = models.SlugField(max_length=64, unique=True)
    type = models.IntegerField(choices=TYPE, default=0)
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    image = models.ImageField(upload_to='images', blank=True)
    image_title = models.CharField(max_length=32, default="Image", blank=True)

    status = models.IntegerField(choices=STATUS, default=0)

    def __str__(self):
        return self.title
# Create your models here.
