from django.db import models

# Create your models here.
class CricketTeam(models.Model):
    name=models.CharField()
    member=models.IntegerField()
    date=models.DateField()
    def __str__(self):
        return self.name