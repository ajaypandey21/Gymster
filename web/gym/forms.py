from django import forms

from .models import GymMem, Admin


class EmpForm(forms.ModelForm):
    class Meta:
        model = GymMem
        fields = ('first_name','last_name','phone','password','email','image')


class AdminForm(forms.ModelForm):
    class Meta:
        model = Admin
        fields = "__all__"
