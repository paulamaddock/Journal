from django.db import models

# Create your models here.
class Entry(models.Model):
    edit_date = models.DateField(auto_now=True)
    entry_date = models.DateField()
    entry_text = models.TextField(max_length=1000)
    project = models.ForeignKey(Project)

class Project(models.Model):
    creation_date = models.DateField()
    project = models.ManyToManyRel()

class Company(models.Model):
    name = models.TextField(max_length=20,unique=True)