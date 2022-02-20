from django.shortcuts import render
from django.http import Http404
from .models import Course


def index(request):
    courses = Course.objects.all()
    context = {"courses": courses}

    return render(request, "courses/index.html", context)


def course_detail(request, course_id):
    try:
        course = Course.objects.get(pk=course_id)
    except Course.DoesNotExist:
        raise Http404("Course not found")

    return render(request, "courses/course_detail.html", {"course": course})
