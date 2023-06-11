import datetime

from django.db import models
from django.utils import timezone
from django.contrib import admin

class Question(models.Model):
    
    question_text = models.CharField(max_length=250)
    date_of_publication = models.DateTimeField("date published")

    def __str__(self):
        return self.question_text


    @admin.display(boolean=True, ordering="date_of_publication", description="Is published recently")
    def was_published_recently(self):

        now = timezone.now()
        #print(type(now), type(datetime.timedelta(days=1)), type(self.date_of_publication))
        return now - datetime.timedelta(days=1) <= self.date_of_publication <= now

class Choice(models.Model):

    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=250)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text