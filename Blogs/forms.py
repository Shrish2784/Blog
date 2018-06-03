from django import forms
from Blogs.models import Post, Comment


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text')
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'posttitleinput',
            }),
            'text': forms.Textarea(attrs={
                'class': 'editable medium-editor-textarea posttextinput',
            })
        }

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('text',)
        widgets = {
            'author': forms.TextInput(attrs={
                'class': 'commentauthorinput'
            }),
            'text': forms.Textarea(attrs={
                'class': 'editable medium-editor-textarea commenttextinput'
            })
        }
