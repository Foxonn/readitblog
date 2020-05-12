from django import forms


class QuillEditor(forms.Widget):
    template_name = 'editor_quill/quill.html'

    def __init__(self, attrs=None):
        super().__init__(attrs={'class': 'quill', **(attrs or {})})

    class Media:
        css = {
            'all': ('https://cdn.quilljs.com/1.3.6/quill.snow.css',)
        }
        js = ['https://cdn.quilljs.com/1.3.6/quill.js', ]
