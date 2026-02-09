from django.db import models

# Create your models here.

class Series(models.Model):
    '''Collection of posts within the same series or topic, e.g. TILs'''

    text = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = 'series'

    def __str__(self):
        return self.text


class Post(models.Model):
    '''Standard blog post'''

    # Mandatory Fields:
    title = models.CharField()
    text = models.TextField()

    # Optional Fields:
    series = models.ManyToManyField(Series, blank=True)

    def __str__(self):
        return self.title
