from django import forms

class MemberForm(forms.Form):
    firstname = forms.CharField(max_length=100)
    lastname = forms.CharField(max_length=100)
    Email = forms.EmailField()
    EBoard = forms.BooleanField(required=False)
