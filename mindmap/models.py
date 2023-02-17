from django.db import models

# Create your models here.


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    value = models.IntegerField(default= 0)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
class Node(models.Model):
    text = models.CharField(max_length= 100)
    x = models.IntegerField()
    y = models.IntegerField()


class Relation(models.Model):
    node1=models.IntegerField()
    node2=models.IntegerField()