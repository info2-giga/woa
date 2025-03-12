from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser


class UserRegistrationForm(UserCreationForm):
    """User registration form, allowing users to register their profile"""

    username = forms.CharField(
        label="Username",
        widget=forms.TextInput(attrs={
            "class": "form-username mei border border-gray-300 focus:ring-blue-500 focus:border-blue-500 rounded-md p-2 w-full"
        }),
    )

    email = forms.EmailField(
        label="Email address",  # Ändere von `forms.CharField` zu `forms.EmailField` für Validierung
        widget=forms.EmailInput(attrs={
            "class": "Email address mei border border-gray-300 focus:ring-blue-500 focus:border-blue-500 rounded-md p-2 w-full"
        }),
    )

    # Passwortfelder
    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={
            "class": "form-password mei border border-gray-300 focus:ring-blue-500 focus:border-blue-500 rounded-md p-2 w-full"
        })
    )
    password2 = forms.CharField(
        label="Password confirmation",
        widget=forms.PasswordInput(attrs={
            "class": "form-password-confirm mei border border-gray-300 focus:ring-blue-500 focus:border-blue-500 rounded-md p-2 w-full"
        })
    )

    profile_image = forms.ImageField(
        label="Profile image",
        required=False,
        widget=forms.FileInput(attrs={
            "class": "form-profile-image mei block"
        })
    )

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'profile_image']

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords do not match")

        return cleaned_data


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(
        label="Username",
        widget=forms.TextInput(attrs={"class": "form-username mei border border-gray-300 focus:ring-blue-500 focus:border-blue-500 rounded-md p-2 w-full"}),
    )
    password = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={"class": "form-password twice border border-gray-300 focus:ring-blue-500 focus:border-blue-500 rounded-md p-2 w-full mb-3"}),
    )


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['bio', 'profile_image']
        widgets = {
            'bio': forms.Textarea(attrs={'class': 'form-textarea rounded border-gray-300 text-gray-700', 'rows': 3}),
            'profile_image': forms.FileInput(attrs={'class': 'form-file-input rounded border-gray-300'}),
        }