from django.db import models
from login.models import user

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
    def __str__(self):
        return self.title
    
class rate(models.Model):
    user = models.ForeignKey('login.user', on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    rate = models.FloatField(default=0)
    def __str__(self):
        return f'{self.user.account} 投了 《{self.movie.title}》 {self.rate}分'
    
class Similar_Item(models.Model):
    movie1 = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='movie1')
    movie2 = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='movie2')
    similar = models.FloatField(default=0)
