from django.http import HttpRequest, Http404
from django.shortcuts import render, get_object_or_404

from .models import Question


def index(request: HttpRequest):
    nearest_questions = Question.objects.order_by("-date_of_publication")[:5]
    context = {
        "nearest_questions": nearest_questions,
    }
    return render(request, "polls/index.html", context)


def detail(request: HttpRequest, question_id):
    question = get_object_or_404(Question, pk=question_id)
    context ={"question": question}
    return render(request, "polls/detail.html", context)


def results(request: HttpRequest, question_id):
    question = Question.objects.get(id=question_id)
    context = {"question": question}
    return render(request, "polls/results.html", context)


def vote(request: HttpRequest, question_id):
    question = Question.objects.get(id=question_id)
    context = {"question": question}
    return render(request, "polls/vote.html", context)
