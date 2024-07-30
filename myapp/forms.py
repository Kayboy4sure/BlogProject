from django import forms
from .models import Message


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['username', 'msg_content',]
        labels = {
            'username': 'Username', 
            'msg_content': 'Message',
        }
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'class': 'col-sm-6'}), 
            'msg_content': forms.Textarea(attrs={'class': 'form-control', 'class': 'col-sm-6'}), 
        }


class Message_editForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['msg_content',]
        labels = { 
            'msg_content': 'Message',
        }
        widgets = {
            'msg_content': forms.Textarea(attrs={'class': 'form-control', 'class': 'col-sm-6'}), 
        }