from django.contrib import admin
from logentries.models import *
# Register your models here.

admin.site.register(Project)
admin.site.register(LogEntry)