from django.db import models

# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date_published')


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)


class Board(models.Model):
    space = models.ImageField()


class Game(models.Model):

    #current_turn = models.ForeignKey(User, related_name='current_turn')
    cols = models.IntegerField(default=8)
    rows = models.IntegerField(default=8)
