from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse('You are in the home page')


def detail(request, question_id):
    return HttpResponse(f'You are accessing to detail of question number {question_id}')


def results(request, question_id):
    return HttpResponse(f'Results of question number {question_id}')


def vote(request, question_id):
    return HttpResponse(f'You are vote to question with the number {question_id}')