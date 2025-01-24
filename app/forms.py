from django import forms
from .models import User

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name', 'gender', 'age', 'purpose', 'opp_gender', 'opp_age', 'personality_1', 'personality_2', 'hobby_1', 'hobby_2']