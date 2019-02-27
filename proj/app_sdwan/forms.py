from django import forms

class ClassForm_Router_Register(forms.Form):
    routerip = forms.CharField()
    username = forms.CharField()
    password = forms.CharField()
