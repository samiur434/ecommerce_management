from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User



class SignUpForm(UserCreationForm):
    password1=forms.CharField(label="Password",max_length='100',widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2=forms.CharField(label="Confirm Password",max_length='100',widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    class Meta:
        model = User
        fields = ('id','username', 'email', 'password1', 'password2')
        labels = {
             'id': 'ID',
            'username': 'Username',
            'email': 'Email',
            'password1': 'Password',
            'password2': 'Confirm Password',
        }
        widgets = {
             'id': forms.TextInput(attrs={'class': 'form-control'}),
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }
        
        


class loginForm(AuthenticationForm):
    
        username=forms.CharField(label="Username",max_length='100',widget=forms.TextInput(attrs={'class': 'form-control'}))
        password=forms.CharField(label="Password",max_length='100',widget=forms.PasswordInput(attrs={'class': 'form-control'}))