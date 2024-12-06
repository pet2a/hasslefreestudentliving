from django.db import models

# Create your models here.
class Student(models.Model):
    fullname = models.CharField(max_length=200)
    username = models.CharField(max_length=200)
    email = models.EmailField()
    password = models.CharField(max_length=20)
    age = models.IntegerField()
    yob = models.DateField()

    def __str__(self):
        return self.fullname

class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.CharField(max_length=50)
    quantity = models.IntegerField()

    def __str__(self):
        return self.name


class Patient(models.Model):
    firstname = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    dateofbirth =models.DateField()
    gender = models.CharField(max_length=20)
    email = models.EmailField()
    phonenumber = models.CharField(max_length=20)
    address = models.CharField(max_length=20)

    def __str__(self):
        return self.firstname + self.lastname

class Appointment(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    date = models.DateTimeField()
    department = models.CharField(max_length=200)
    doctor = models.CharField(max_length=200)
    message = models.TextField()

    def __str__(self):
        return self.name

class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    subject = models.CharField(max_length=20)
    message = models.TextField()

    def __str__(self):
        return self.name

class Member(models.Model):
    name = models.CharField(max_length=200)
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class ImageModel(models.Model):
    image = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=50)
    price = models.CharField(max_length=50)

    def __str__(self):
        return self.title