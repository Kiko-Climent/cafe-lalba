from django import forms
from allauth.account.forms import LoginForm
from allauth.account.forms import SignupForm as AllauthSignupForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import get_user_model
from .models import ContactMessage
from django.utils.translation import ugettext_lazy as _

User = get_user_model()


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'subject', 'email', 'notes']


class CustomSignupForm(AllauthSignupForm):
    first_name = forms.CharField(max_length=30, label=_('First Name'))
    last_name = forms.CharField(max_length=30, label=_('Last Name'))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].required = True

    def save(self, request):
        user = super().save(request)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()
        return user


class CustomLoginForm(AuthenticationForm):
    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        user = None

        if username and password:
            user = authenticate(username=username, password=password)

            if user is None:
                raise forms.ValidationError("Invalid username or password")

            self.user = user

        return self.cleaned_data
