from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField()
    rollno=models.IntegerField()
    enroll=models.IntegerField()
    batch=models.CharField()
    date=models.DateField()
    image=models.ImageField(upload_to='students')
    def __str__(self):
        return self.name