from django.contrib import admin
from .models import Course, Challenge, Step, StepProgress


class ChallengeInline(admin.TabularInline):
    model = Challenge
    extra = 1


class CourseAdmin(admin.ModelAdmin):
    list_display = ("title", "created_at", "author")
    inlines = [ChallengeInline]


admin.site.register(Course, CourseAdmin)


class StepInline(admin.TabularInline):
    model = Step
    extra = 1


class ChallengeAdmin(admin.ModelAdmin):
    list_display = ("title", "order", "course")
    inlines = [StepInline]


admin.site.register(Challenge, ChallengeAdmin)


class StepAdmin(admin.ModelAdmin):
    list_display = ("title", "order", "challenge")


admin.site.register(Step, StepAdmin)
admin.site.register(StepProgress)
