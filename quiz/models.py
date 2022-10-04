from django.db import models

# Create your models here.
class Word(models.Model):
  english = models.CharField(max_length=30)
  korean = models.CharField(max_length=30)

  def __str__(self):
    return self.english + ' : ' + self.korean


class Score(models.Model):
  score = models.IntegerField()
  total_score = models.IntegerField()

  def __str__(self):
    return str(self.score) + '/' + str(self.total_score)