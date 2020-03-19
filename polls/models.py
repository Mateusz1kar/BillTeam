from django.db import models

# Create your models here.
from django.forms import forms


class Person(models.Model):
    idPerson = models.AutoField(primary_key=True)
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    login = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    position = models.CharField(max_length=50)

    admin = models.BooleanField(default=0)

    def __str__(self):
        return ""+self.idPerson.__str__() + " "+self.firstName + " "+self.lastName + " "+self.login + " "+self.position + " "+self.admin.__str__() + " "


class Project(models.Model):
    idProject = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    owner = models.ForeignKey(Person,on_delete=models.SET_NULL,null=True)
    state = models.CharField(max_length=50)


class Notification(models.Model):
    idNotification = models.AutoField(primary_key=True)
    who = models.ForeignKey(Person, on_delete=models.SET_NULL,null=True)
    what = models.CharField(max_length=100)
    projectOwner = models.ForeignKey(Project,on_delete=models.CASCADE)




