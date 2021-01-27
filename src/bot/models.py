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

class User(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    type_work = models.IntegerField()
    created_at = models.DateTimeField(auto_now=True, blank=True)
    update_at = models.DateTimeField(auto_now=True, blank=True)

    def __str__(self):
        return self.first_name
    