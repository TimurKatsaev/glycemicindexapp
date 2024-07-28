from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    rcg = models.TextField(blank=True)
    absorption_time = models.TextField(blank=True)

    def __str__(self):
        return self.username

class Note(models.Model):
    title = models.CharField(max_length=300)
    content = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    glycemia = models.FloatField()
    bread_units = models.FloatField(blank=True)
    glycemic_index = models.CharField(max_length=10)
    general_gi = models.FloatField()
    general_rcg = models.FloatField()
    graph = models.TextField()
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

class Statistics(models.Model):
    average_glycemia = models.FloatField(blank=True)
    average_bu = models.FloatField(blank=True)
    average_gi = models.FloatField(blank=True)
    average_rcg = models.FloatField(blank=True)
    graph_glycemia = models.TextField(blank=True)
    graph_bu = models.TextField(blank=True)
    graph_gi = models.TextField(blank=True)
    graph_rcg = models.TextField(blank=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)  