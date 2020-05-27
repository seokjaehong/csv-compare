from django.contrib import admin

# Register your models here.
from cjudge.models import Submission


class SubmissionAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Submission._meta.fields]


admin.site.register(Submission, SubmissionAdmin)

