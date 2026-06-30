from django.db import models

# Create your models here.
class Department(models.Model):
    hod_name=models.CharField()
    dep_name=models.CharField()

    def __str__(self):
        return self.dep_name

class Student(models.Model):
    name=models.CharField()
    enroll=models.IntegerField()
    email=models.CharField()
    department=models.ForeignKey(Department,on_delete=models.CASCADE)

    def __str__(self):
        return self.name