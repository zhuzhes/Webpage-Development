from django import forms
from app_sdwan.models import ClassModel_Router_Register
# class ClassForm_Router_Register(forms.Form):
#     routerip = forms.CharField()
#     username = forms.CharField()
#     password = forms.CharField()

class ClassForm_Router_Register(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = ClassModel_Router_Register
        fields = "__all__"

class ClassForm_Router_Delete(forms.Form):
    routerip = forms.CharField()
