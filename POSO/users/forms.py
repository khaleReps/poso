from django import forms

class EmailLoginSettingsForm(forms.Form):
    email_host = forms.CharField(label='Email Host')
    email_port = forms.IntegerField(label='Email Port')
    email_use_ssl = forms.BooleanField(label='Use SSL', required=False)
