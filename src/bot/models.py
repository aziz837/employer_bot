from django.db import models

class Category(models.Model):
    title = models.CharField(max_length=80 )
    parend_id = models.IntegerField( null=True, blank=False)
    last_time = models.DateTimeField(auto_now=True, blank=True)

    def __str__(self):
        return self.title

class Region(models.Model):
    title = models.CharField(max_length=80 )
    parend_id = models.IntegerField( null=True, blank=False)

    def __str__(self):
        return self.title