from django import forms
from .models import Comment


class CommentForm(forms.Form):
    name = forms.CharField(max_length=75,)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea,)
    post = forms.IntegerField()
    replys = forms.IntegerField(widget=forms.NumberInput, required=False)
