from django import forms

from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title','pic','brief', 'content']

        widgets = {
            'content': forms.Textarea(attrs={'class': 'editable medium-editor-textarea'})
        }
