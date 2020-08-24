from django import forms
from .models import LikeComment, Blike

class CommentForm(forms.ModelForm):
    #text = forms.TextInput(label = '댓글')

    class Meta:
        model = LikeComment
        fields = ['text']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['text'].label = "댓글"