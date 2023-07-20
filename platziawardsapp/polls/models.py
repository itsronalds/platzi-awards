from django.db import models

'''
    # Concepts:

    - on_delete=models.CASCADE: When we delete a Question, the options will be deleted
'''


class Question(models.Model):
    question_text = models.TextField
    date = models.DateTimeField('Date published')


class Choice(models.Model):
    question_id = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.TextField
    votes = models.BigIntegerField(default=0)