from django.db import models
from django import forms
from .widgets import CKEditor5Widget


class CKEditor5Field(models.TextField):
    def __init__(self, *args, **kwargs):
        super(CKEditor5Field, self).__init__(*args, **kwargs)

    def formfield(self, **kwargs):
        """Get the form for field."""
        defaults = {
            'form_class': CKEditor5FormField,
        }
        defaults.update(kwargs)
        return super(CKEditor5Field, self).formfield(**defaults)


class CKEditor5FormField(forms.fields.CharField):
    """Extend form field for CKEditor5."""

    def __init__(self, *args, **kwargs):
        kwargs.update({
            'widget': CKEditor5Widget()
        })
        super(CKEditor5FormField, self).__init__(*args, **kwargs)
