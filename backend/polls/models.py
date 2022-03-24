from django.db import models

# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    
class Movie(models.Model):
    title = models.CharField(max_length=200)
    oth_title = models.CharField(max_length=200)
    category = models.CharField(max_length=200)
    rating_num = models.FloatField(default=0)
    picture = models.CharField(max_length=200)