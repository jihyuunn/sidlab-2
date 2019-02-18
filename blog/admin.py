from django.contrib import admin
from .models import Publication, Project, People

admin.site.register(Publication)
admin.site.register(Project)
admin.site.register(People)