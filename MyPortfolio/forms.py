from django import forms
from django.contrib.auth.models import User
from .models import portfolios


class PortfolioForm(forms.ModelForm):
    class Meta:
        model = portfolios
        fields = [
            'full_name',
            'bio',
            'phone',
            'email',
            'github',
            'linkedin',
            'about',
            'skills',   
            
            'services',
        ]


class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']



from django import forms
from .models import Project

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'description', 'github_link', 'live_link']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Project Title'}),
            'description': forms.Textarea(attrs={'placeholder': 'Project Description'}),
            'github_link': forms.URLInput(attrs={'placeholder': 'GitHub URL'}),
            'live_link': forms.URLInput(attrs={'placeholder': 'Live Demo URL'}),
        }
