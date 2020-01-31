from django import forms
from emailsender.models import Email


class SendEmailForm(forms.ModelForm):
    class Meta:
        model = Email
        fields = '__all__'
