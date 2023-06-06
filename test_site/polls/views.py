from django.http import HttpResponse, HttpRequest
from django.template import loader

from .models import Question, Choice


def index(request: HttpRequest):
    nearest_questions = Question.objects.order_by("-date_of_publication")[:5]
    template = loader.get_template("polls/index.html")
    context = {
        "nearest_questions": nearest_questions,
    }
    return (HttpResponse(template.render(context, request)))


def detail(request: HttpRequest, question_id):
    response = "There is a next question: {} "
    return HttpResponse(response.format(question_id))


def results(request: HttpRequest, question_id):
    response = "There is a result of next question: {} "
    return HttpResponse(response.format(question_id))


def vote(request: HttpRequest, question_id):
    response = "You are voting on question: {} "
    return HttpResponse(response.format(question_id))
