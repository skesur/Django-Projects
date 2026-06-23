from django.db import models

# Create your models here.
class movies(models.Model):
    name=models.CharField()
    release_date=models.DateField()
    director=models.CharField()
    review=models.IntegerField()
    description=models.CharField()
    actor=models.CharField()

    def __str__(self):
        return self.name