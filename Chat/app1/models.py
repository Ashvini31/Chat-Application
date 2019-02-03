from django.db import models

#Making different table in the database also specifying the length and type.

class admindata (models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    contact = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100, default='null')

#Creating string representation of the object

    def __str__(self):
        return self.name

class signupdata (models.Model):
    fullname = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100, default='null')

    def __str__(self):
        return self.fullname

class logindata (models.Model):
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    usertype = models.CharField(max_length=100, default='null')

    def __str__(self):
        return self.email