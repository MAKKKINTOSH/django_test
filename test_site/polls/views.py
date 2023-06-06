from django.http import HttpResponse, HttpRequest
from django.shortcuts import render

from .models import Question, Choice


def index(request: HttpRequest):
    nearest_questions = Question.objects.order_by("-date_of_publication")[:5]
    context = {
        "nearest_questions": nearest_questions,
    }
    return render(request, "polls/index.html", context)


def detail(request: HttpRequest, question_id):
    question = Question.objects.filter(id=question_id)[0]
    context ={"question": question}
    return HttpResponse(render(request, "polls/detail.html", context))


def results(request: HttpRequest, question_id):
    question = Question.objects.filter(id=question_id)[0]
    context = {"question": question}
    return HttpResponse(render(request, "polls/results.html", context))


def vote(request: HttpRequest, question_id):
    question = Question.objects.filter(id=question_id)[0]
    context = {"question": question}
    return HttpResponse(render(request, "polls/vote.html", context))
