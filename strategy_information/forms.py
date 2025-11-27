from django import forms
from .models import Strategy, Comment

class StrategyForm(forms.ModelForm):
    class Meta:
        model = Strategy
        fields = ["title", "content", "image"]

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["text"]

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, label="お名前")
    email = forms.EmailField(label="メールアドレス")
    message = forms.CharField(widget=forms.Textarea, label="お問い合わせ内容")