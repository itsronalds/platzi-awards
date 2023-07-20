from django.db import models
from django.utils import timezone

from datetime import timedelta

'''
    # Concepts:

    - on_delete=models.CASCADE: When we delete a Question, the options will be deleted
'''


class Question(models.Model):
    question_text = models.CharField(max_length=255, default='')
    date = models.DateTimeField('Date published', auto_now_add=True)


    def __str__(self):
        return self.question_text
    

    def was_published_recently(self):
        return self.date >= (timezone.now() - timedelta(days=1))


class Choice(models.Model):
    question_id = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=255, default='')
    votes = models.BigIntegerField(default=0)