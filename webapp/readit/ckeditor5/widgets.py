from django import forms
from django.conf import settings
import json
from string import Template


class CKEditor5Widget(forms.Widget):
    template_name = 'ckeditor5/ckeditor5.html'

    def render(self, name, value, attrs=None, renderer=None):
        return renderer.render(self.template_name, {
            'value': value,
            'name': name,
            'settings': json.dumps(getattr(settings, 'CKEDITOR5_CONFIGS')),
        });
