from django.db import models

# Create your models here.


class Note(models.Model):
    text = models.TextField(null=True, blank=True, max_length=2000)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text[0:100] # only returns the first 100 characters (notes can be longer)

