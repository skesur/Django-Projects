from django.db import models

# Create your models here.
class Cricket(models.Model):
    team=models.CharField()
    run=models.IntegerField()
    cap=models.CharField()
    date=models.DateField()
    def __str__(self):
        return self.team