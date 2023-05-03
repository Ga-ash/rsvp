from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.utils import timezone
from django.views import generic
from django.shortcuts import render

from .models import Choice, Question, UsedPassword
import base64
import zlib


def vulnerable_verify_hash(text):
    chars = [chr(i) for i in range(ord("A"), ord("Z") + 1)] + [str(i) for i in range(6)]
    text = (32 - len(str(bin(zlib.crc32(base64.b64decode(text))))[2:])) * "0" + str(
        bin(zlib.crc32(base64.b64decode(text)))
    )[2:]
    return (
        "".join([chars[int(text[i : i + 5], 2)] for i in range(0, len(text), 5)])[:5]
        == "GAASH"
    )


class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        """
        Return the last five published questions (not including those set to be
        published in the future).
        """
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by(
            "-pub_date"
        )[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = "polls/detail.html"

    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())


class ResultsView(generic.DetailView):
    model = Question
    template_name = "polls/results.html"


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    password_valid = False
    password = ""
    if request.method == "POST":
        password = request.POST.get("password")
        is_used = UsedPassword.objects.filter(value=password).exists()
        if is_used:
            return render(
                request,
                "polls/detail.html",
                {
                    "question": question,
                    "error_message": "Revoked password.",
                    "password_valid": False,
                },
            )

        if vulnerable_verify_hash(password):
            password_valid = True
    if not password_valid:
        return render(
            request,
            "polls/detail.html",
            {
                "question": question,
                "error_message": "Invalid password.",
                "password_valid": False,
            },
        )
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        return render(
            request,
            "polls/detail.html",
            {
                "question": question,
                "error_message": "You didn't select a choice.",
            },
        )
    else:
        selected_choice.votes += 1
        selected_choice.save()
        used_password = UsedPassword(value=password)
        used_password.save()
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))
