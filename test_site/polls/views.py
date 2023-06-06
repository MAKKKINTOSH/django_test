from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from .models import Question, Choice


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
    question = Question.objects.get(pk=question_id)
    context = {"question": question}
    return render(request, "polls/results.html", context)


def vote(request: HttpRequest, question_id):

    question = Question.objects.get(id=question_id)
    context = {
        "question": question,
        "error_message": "You didn't select a choice!"
    }

    try:
        print(request.POST, request.GET, request.META, sep="\n")
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except(KeyError, Choice.DoesNotExist):
        return render(
            request,
            "polls/detail.html",
            context
        )
    else:
        selected_choice.votes+=1
        selected_choice.save()
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))