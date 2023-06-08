from django.test import TestCase
import datetime
from django.utils import timezone
from django.urls import reverse

from .models import Question


class QuestionModelTests(TestCase):
    def test_was_published_recently_with_future_question(self):
        time = (timezone.now() + datetime.timedelta(days=30)).timestamp()
        fq = Question(date_of_publication=time)
        self.assertIs(fq.was_published_recently(), False)

    def test_was_published_recently_with_old_question(self):
        time = (timezone.now() - datetime.timedelta(days=1, seconds=1)).timestamp()
        old_question = Question(date_of_publication=time)
        self.assertIs(old_question.was_published_recently(), False)

    def test_was_published_recently_with_recent_question(self):
        time = (timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)).timestamp()
        old_question = Question(date_of_publication=time)
        self.assertIs(old_question.was_published_recently(), True)


def create_question(question_text, days):
    """days sets the timedelta"""
    time = timezone.now() + datetime.timedelta(days=days)
    return (Question.objects.create(question_text=question_text, date_of_publication=time))

class QuestionIndexViewTest(TestCase):
    def test_no_questions(self):

        response = self.client.get(reverse("polls:index"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No polls are available!")
        self.assertQuerySetEqual(response.context["nearest_questions"], [])

    def test_past_question(self):

        q = create_question("Past question", -30)
        response = self.client.get(reverse("polls:index"))
        self.assertQuerySetEqual(response.context["nearest_questions"], [q])

    def test_future_question(self):

        create_question("Future question", 30)
        response = self.client.get(reverse("polls:index"))
        self.assertContains(response, "No polls are available!")
        self.assertQuerySetEqual(response.context["nearest_questions"], [])

    def test_future_question_and_past_question(self):

        question = create_question("Past question.", -30)
        create_question("Future question.", 30)
        response = self.client.get(reverse("polls:index"))
        self.assertQuerySetEqual(response.context["nearest_questions"], [question])

    def test_two_past_questions(self):

        q1 = create_question("Past question 1", -30)
        q2 = create_question("Past question 2", -20)
        print(q2.date_of_publication)
        response = self.client.get(reverse("polls:index"))
        self.assertQuerySetEqual(response.context["nearest_questions"], [q2, q1])

class QuestionDetailViewTests(TestCase):
    def test_future_question(self):

        fq = create_question("Future_question", 5)
        url = reverse("polls:detail", args=(fq.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_past_question(self):

        past_question = create_question("Past Question", -5)
        url = reverse("polls:detail", args=(past_question.id,))
        response = self.client.get(url)
        self.assertContains(response, past_question.question_text)