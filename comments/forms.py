from django import forms
from comments.models import Comment
class CommentForm(forms.Form):
    #parent_id = forms.IntegerField(widget=forms.HiddenInput, required=False)
    content = forms.CharField(label='',widget=forms.Textarea(attrs={'placeholder':'Enter a comment...'}))

    class Meta:
        model = Comment
        fields = ['content',]