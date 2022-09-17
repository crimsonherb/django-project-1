from socket import fromshare
from django import forms
from recipe_crud.models import Post


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('recipe_name','ingredients','author','direction','thumbnail')

        widgets = {
            'ingredients': forms.Textarea(attrs={'class': 'editable medium-editor-textarea postcontent'}),
            'direction': forms.Textarea(attrs={'class': 'editable medium-editor-textarea postcontent'}),
        }