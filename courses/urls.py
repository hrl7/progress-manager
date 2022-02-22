from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("courses/<int:course_id>/", views.course_detail, name="course_detail"),
    path(
        "challenges/<int:challenge_id>/",
        views.challenge_detail,
        name="challenge_detail",
    ),
]
