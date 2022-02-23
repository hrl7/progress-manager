from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("courses/<int:course_id>/", views.course_detail, name="course_detail"),
    path(
        "challenges/<int:challenge_id>/",
        views.challenge_detail,
        name="challenge_detail",
    ),
    path("login", auth_views.LoginView.as_view(template_name="login.html")),
    path("logout", auth_views.LogoutView.as_view(template_name="logout.html")),
]
