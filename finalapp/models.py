from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Admin(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200)
    image = models.ImageField(upload_to='static', null=True, blank=True)

    def __str__(self):
        return self.name


class field(models.Model):
    username = models.CharField(max_length=200)
    email = models.EmailField()
    password = models.CharField(max_length=200)

    class Meta:
        db_table = "field"


class login(models.Model):
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)

    class Meta:
        db_table = "login"


class Country(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name


class City(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name


class Person(models.Model):
    name = models.CharField(max_length=124)
    email = models.EmailField()
    phoneNumber = models.PositiveIntegerField()
    gender = models.CharField(max_length=250)
    date = models.DateField()
    address = models.CharField(max_length=250)
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, blank=True, null=True)
    city = models.ForeignKey(City, on_delete=models.SET_NULL, blank=True, null=True)

    class Meta:
        db_table = "Person"

    def __str__(self):
        return self.name
