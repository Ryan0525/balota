from django import forms
from django.forms import ModelForm
from .models import Member_info, Program


class MemberForm(forms.ModelForm):
    class Meta:
        model = Member_info
        fields = '__all__'

class ProgramForm(forms.ModelForm):
    class Meta:
        model = Program
        fields = '__all__'

