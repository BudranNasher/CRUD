from django.db import models

class Student(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200, unique=True)
    age = models.IntegerField()
    city = models.CharField(max_length=200)
    gpa = models.DecimalField(max_digits=3, decimal_places=2)

    def __str__(self):
        return self.name
