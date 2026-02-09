from django.contrib import admin

# Register your models here.

from .models import Series, Post

admin.site.register(Series)
admin.site.register(Post)
