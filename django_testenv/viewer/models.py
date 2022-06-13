from django.db import models
from django.contrib.auth.models import User, Group
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class organisation(models.Model):
    users = models.ForeignKey(User, on_delete=models.CASCADE)
    organisation_name = models.TextField(max_length=500, blank=True)

    def __str__(self):
        return self.organisation_name

class customisation(models.Model):
    background_image = models.CharField(max_length=250, null=True)
    logo_image = models.CharField(max_length=250, null=True)
    organisation = models.ForeignKey(Group, on_delete=models.CASCADE)

    def __str__(self):
        return self.background_image

class Page(models.Model):
    data_location = models.URLField()
    page_name = models.CharField(max_length=250)
    organisation = models.ForeignKey(Group, on_delete=models.CASCADE)
    page_description = models.CharField(max_length=500, null=True)

    def __str__(self):
        return self.page_name

class Pointcloud(models.Model):
    name = models.CharField(max_length=250)
    page = models.ForeignKey(Page, on_delete=models.SET_NULL, related_name='Pointcloud',null=True)

    def __str__(self):
        return self.name



