from django.shortcuts import render
from django.http import Http404
from .models import Course, Challenge


def index(request):
    courses = Course.objects.all()
    context = {"courses": courses}

    return render(request, "courses/index.html", context)


def course_detail(request, course_id):
    try:
        course = Course.objects.get(pk=course_id)
        course.challenges = course.challenge_set.all()
    except Course.DoesNotExist:
        raise Http404("Course not found")

    return render(
        request,
        "courses/course_detail.html",
        {"course": course},
    )


def challenge_detail(request, challenge_id):
    try:
        challenge = Challenge.objects.get(pk=challenge_id)
    except Challenge.DoesNotExist:
        raise Http404("Challenge not found")

    return render(request, "courses/challenge_detail.html", {"challenge": challenge})
