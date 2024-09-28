from django.contrib import admin, sites

# Register your models here.
from .models import (
    Skill,
    JobPost,
)

admin.site.register(Skill)
admin.site.register(JobPost)
