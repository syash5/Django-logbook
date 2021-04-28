from django.urls import path
from logentries.views import add_log, projectcreate, show

urlpatterns = [
    path('project-create/', projectcreate, name="project-create"),
    path('addlog/', add_log, name="addlog"),
    path('show/', show, name="show"),
    path('', show, name="show"),
]