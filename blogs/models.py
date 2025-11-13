from django.db import models
from django.contrib.auth.models import User



class Integration(models.Model):
    type_choices = ("goodreads","goodreads"),("trakt","trakt")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    integration_type = models.CharField(max_length=20, choices=type_choices)
    integration_url = models.URLField(max_length=200)
    last_sync = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



    def __str__(self):
        return f"{self.integration_type} - {self.integration_url}"


class Activity(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    activity_type = models.CharField(max_length=20)
    activity_detail = models.JSONField(max_length=500,null=True)
    image = models.ImageField(null=True,blank=True)
    url = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return self.activity_type
