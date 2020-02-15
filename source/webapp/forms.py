from django import forms

from webapp.models import Comment


class PostCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['user', 'text']


