from django import forms

class SubmissionForm(forms.Form):
    docfile = forms.FileField(
        label='select a file',
        help_text='max. 25 megabytes'
    )

