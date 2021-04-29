from django import forms
from django.contrib.auth.forms import UserCreationForm
from logentries.models import LogEntry, Project


class ProjectCreateForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = [ 'project']

class DateInput(forms.DateInput):
    input_type = 'date'

class LogCreationForm(forms.ModelForm):
    # body = forms.CharField()
    # startt = forms.SplitDateTimeField()
    # endt = forms.SplitDateTimeField()
    # project = forms.ModelMultipleChoiceField(queryset=Project.objects.all(),widget=forms.CheckboxSelectMultiple())

    class Meta:
        model = LogEntry
        fields = [ 'body','startt' ,'endt' ,'project', 'user']
        widgets = {'user': forms.HiddenInput()}
        labels = {
            'body': ('Describe Task'),
            'startt': ('Start Date'),
            'endt': ('End Date'),
            'project': ('Project Name'),
        }
        help_texts = {
            # 'body': ('Write Here'),
            'startt': ('YYYY-MM-DD HH:MM:SS' ),
            'endt': ('YYYY-MM-DD HH:MM:SS'),
            # 'project': ('Write Here'),
        }
        # widgets = {
        #     'startt': DateInput(),
        # }