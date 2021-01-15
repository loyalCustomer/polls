from django.db import models
from django.utils import timezone

# Create your models here.c.
class Question(models.Model):
    question_text = models.CharField (max_length=200)
    pub_date = models.DateTimeField ('date published',default=timezone.now())
    event = models.CharField(max_length=200, default ='not specified')
    expiration_date = models.DateField ('expire:',default=timezone.now)

    def __str__(self):
        return self.question_text 
2
class Choice (models.Model):
    question_text = models.ForeignKey (Question, on_delete = models.CASCADE)
    choice_text = models.CharField(max_length = 200)
  #  choice_text2 = models.CharField(max_length=200,default='not worked for me')
    vote = models.IntegerField(default = 0)
    
    def __str__(self):
        return self.choice_text
