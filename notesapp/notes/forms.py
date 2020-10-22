from django import forms
from django.core.exceptions import ValidationError
from .models import Note

class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = [
            'title',
            'body'
        ]

class ContactForm(forms.Form):
    class Meta:
        email = forms.EmailField(required=True)
        title = forms.CharField(required=True, max_length=255)
        body = forms.CharField(label="Your message", widget=forms.Textarea(attrs={'required': True}))

class SearchForm(forms.Form):
    SEARCH_TYPES_CHOICES = (
        ("starts with", "starts with"),
        ("includes", "includes"),
        ("exact match", "exact match"),
    )
    ORDER_CHOICES = (
        ("title", "title"),
        ("body", "body"),
    )
    title = forms.CharField(max_length=255, required=True)
    title_search_type = forms.ChoiceField(choices=SEARCH_TYPES_CHOICES, label="Search Title for", required=True)
    body = forms.CharField(widget=forms.Textarea, required=False)
    body_search_type = forms.ChoiceField(choices=SEARCH_TYPES_CHOICES, label="Search Body for", required=True)
    order_by = forms.ChoiceField(choices=ORDER_CHOICES, required=True)

def clean(self):
    cleaned_data = super().clean()
    cleaned_title = cleaned_data['title']
    cleaned_body = cleaned_data['body']
    if cleaned_title or cleaned_body:
        return cleaned_data
    raise ValidationError('Please specify one of the fields, code="invalid')        