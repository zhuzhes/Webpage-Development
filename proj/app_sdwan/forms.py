from django import forms
from app_sdwan.models import *
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

class ClassForm_Router_pingresult(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = ClassModel_Router_pingresult
        fields = ("mgtIP","username","password","destinationIP")

class ClassForm_Router_Interface(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = ClassModel_Router_Interface
        fields = ("mgtIP","username","password")

class ClassForm_Router_Interface_Save(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = ClassModel_Router_Interface
        fields = "__all__"
