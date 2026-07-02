from django.db import models

# Create your models here.
class Company(models.Model):
    name=models.CharField()
    year=models.IntegerField()
    location=models.CharField()
    def __str__(self):
        return self.name
    
class Employee(models.Model):
    e_name=models.CharField()
    email=models.EmailField()
    designation=models.CharField()
    salary=models.IntegerField()
    company=models.ForeignKey(Company,on_delete=models.CASCADE)
    def __str__(self):
        return self.e_name