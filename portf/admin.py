from django.contrib import admin
from portf.models import Project
from blog.models import Blog#that class in my model that i wanna display
# Register your models here.

admin.site.register(Project)
admin.site.register(Blog)