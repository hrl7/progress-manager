from django.contrib import admin
from .models import Course, Challenge, Step, StepProgress

admin.site.register(Course)
admin.site.register(Challenge)
admin.site.register(Step)
admin.site.register(StepProgress)

