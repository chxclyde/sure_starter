from django.db import models

# Create your models here.



class Node(models.Model):
    text = models.CharField(max_length= 100)
    x = models.IntegerField()
    y = models.IntegerField()
    type = models.CharField(max_length=100)

class Relation(models.Model):
    node1=models.IntegerField()
    node2=models.IntegerField()