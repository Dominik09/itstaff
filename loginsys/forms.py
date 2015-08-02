from django import forms
from .models import User
from django.contrib.auth.forms import UserChangeForm, UserCreationForm


class AdminUserAddForm(UserCreationForm):
    class Meta:
        model = User
        fields = '__all__'

    def clean_username(self):
        username = self.cleaned_data['username']
        try:
            User.objects.get(username = username)
        except User.DoesNotExist:
            return username
        raise forms.ValidationError(self.error_messages['duplicate_username'])


class AdminUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = '__all__'


class RegistrationForm(forms.ModelForm):
    error_messages = {
        'password_mismatch': ("The two password fields didn't match."),
    }

    class Meta():
        model = User
        fields = ('username', 'first_name', 'last_name', 'email',)

    password1 = forms.CharField(label="Пароль", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Подтверждение пароля", widget=forms.PasswordInput)

    def clean_password2(self):
        # Сверяет пароли
        pass1 = self.cleaned_data.get('password1')
        pass2 = self.cleaned_data.get('password2')
        if pass1 and pass2 and pass1 != pass2:
            raise forms.ValidationError(
                    'Пароли не совпадают',
                    code = 'password_mismatch',
                )
        return pass2

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user