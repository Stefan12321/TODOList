from django import forms
from datetime import datetime


class AddTaskForm(forms.Form):
    task = forms.CharField(label="Describe the task",
                           widget=forms.widgets.Textarea(attrs={"class": "form-control"}))
    deadline = forms.DateTimeField(label="Set the deadline",
                                   initial=format(datetime.today()),
                                   widget=forms.widgets.DateTimeInput(attrs={"type": "datetime-local",
                                                                             "class": "form-control"}))