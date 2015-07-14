from django import forms
from loginsys.models import User

class RegistrationForm(forms.ModelForm):
    class Meta():
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'birth_date',
            'specialization',
            'about_youself',
            'gender',
        ]

    password1 = forms.CharField(label="Password",
    widget=forms.PasswordInput)
    password2 = forms.CharField(label="Password confirmation",
    widget=forms.PasswordInput)