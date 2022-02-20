from asyncio import constants
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Course(models.Model):
    title = models.CharField(max_length=512, unique=True)
    created_at = models.DateTimeField("date created", default=timezone.now)
    updated_at = models.DateTimeField("date updated", null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title}"


class Challenge(models.Model):
    title = models.CharField(max_length=512)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    description = models.TextField(default="")
    created_at = models.DateTimeField("date created", default=timezone.now)
    updated_at = models.DateTimeField("date updated", null=True)
    order = models.IntegerField()

    def __str__(self):
        return f"{self.title}"

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["course", "title"], name="challenge_title_unique"
            ),
            models.UniqueConstraint(
                fields=["course", "order"], name="challenge_order_unique"
            ),
        ]


class Step(models.Model):
    challenge = models.ForeignKey(Challenge, on_delete=models.CASCADE)
    title = models.CharField(max_length=1024)
    body = models.TextField(default="")
    order = models.IntegerField()
    created_at = models.DateTimeField("date created", default=timezone.now)
    updated_at = models.DateTimeField("date updated", null=True)

    def __str__(self):
        return f"{self.title}"

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["challenge", "order"], name="step_unique"),
            models.UniqueConstraint(
                fields=["challenge", "title"], name="step_title_unique"
            ),
        ]


class StepProgress(models.Model):
    STEP_STATUS = [
        ("TODO", "Todo"),
        ("DOING", "Doing"),
        ("DONE", "Done"),
        ("GAVE_UP", "Gave up"),
        ("STUCKED", "Stucked"),
        ("PENDING", "Pending"),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    step = models.ForeignKey(Step, on_delete=models.CASCADE, null=False)
    state = models.CharField(max_length=20, choices=STEP_STATUS, null=False)
    created_at = models.DateTimeField("date created", default=timezone.now)
    updated_at = models.DateTimeField("date updated", null=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["user", "step"], name="progress_step_user_unique"
            ),
        ]
