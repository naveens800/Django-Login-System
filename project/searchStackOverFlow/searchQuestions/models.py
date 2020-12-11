from django.db import models

# Create your models here.
class Question(models.Model):

    QUESTIONS_BY_FIELDS = [
        ('NO_ANS','no-answers'),  #questions with no answers
        ('UN_ANS','un_answered'), #questions that site considers unanswered 
        ('DEFAULT','default'),    #questions without any fields 
        ('FEATURED','featured'),  #questions that are featured in site
        ('RELATED','related'),    #questions that are related to set of ids
        ('LINKED','linked'),      #question that are linked to set of ids
    ]
    question = models.CharField(max_length=50,choices=QUESTIONS_BY_FIELDS,default='DEFAULT')
    ids      = models.CharField(max_length=50,blank=True) #to specify set of ids for questions

    def __str__(self):
        return self.id
