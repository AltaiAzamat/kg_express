from django import forms

from .models import User



class LoginForm(forms.Form):
    email = forms.EmailField(
        label="эдектронная почта",
        widget=forms.EmailInput(attrs={"class":"form-control"})
    )
    password = forms.CharField(
        label="пароль",
        widget=forms.PasswordInput(attrs={"class":"form-control"})
    )
class UserRegisterForm(forms.ModelForm):
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            "class":"form-control"
        })
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            "class":"form-control"}))
    class Meta:
        model = User
        fields = [
            'email',
            'first_name',
            'last_name',
            'middle_name',
            'phone',
            'avatar',
            'password',
        ]

    def clean_password2(self):
        cd = self.cleaned_data  #{"email":"admin@gmail.com"}
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Пароли не совпадают')
        return cd['password2']