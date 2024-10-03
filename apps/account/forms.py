from django import forms
from django.core.validators import validate_email
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError

User = get_user_model()


class UserRegistrationForm(forms.ModelForm):
    fname = forms.CharField(
        label="First Name",
        widget=forms.TextInput(
            attrs={
                "class": "input w-full",
                "placeholder": "Enter your first name",
                "autocomplete": "given-name",
            }
        ),
    )
    lname = forms.CharField(
        label="Last Name",
        widget=forms.TextInput(
            attrs={
                "class": "input w-full",
                "placeholder": "Enter your last name",
                "autocomplete": "family-name",
            }
        ),
    )
    email = forms.EmailField(
        label="Email",
        widget=forms.EmailInput(
            attrs={
                "class": "input w-full",
                "placeholder": "Enter your email",
                "autocomplete": "email",
            }
        ),
    )
    password = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(
            attrs={
                "class": "password-field pr-10 w-full",
                "placeholder": "Enter a password",
            }
        ),
    )
    confirm_password = forms.CharField(
        label="Confirm Password",
        widget=forms.PasswordInput(
            attrs={
                "class": "password-field pr-10 w-full",
                "placeholder": "Enter the password again",
            }
        ),
    )

    class Meta:
        model = User
        fields = ["fname", "lname", "email", "password", "confirm_password"]

    def clean_required_fields(self, field_name, label):
        value = self.cleaned_data.get(field_name)
        if not value:
            raise ValidationError(f"{label} is required.")
        return value

    def clean_fname(self):
        return self.clean_required_fields("fname", label="First name")

    def clean_lname(self):
        return self.clean_required_fields("lname", label="Last name")

    def clean_email(self):
        email = self.clean_required_fields("email", label="Email")
        validate_email(email)
        if User.objects.filter(email=email).exists():
            raise ValidationError("A user with this email already exists.")
        return email

    def clean_password(self):
        password = self.clean_required_fields("password", label="Password")
        if password and len(password) < 8:
            raise ValidationError("Password must be at least 8 characters long.")
        return password

    def clean_confirm_password(self):
        return self.clean_required_fields("confirm_password", label="Confirm password")

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise ValidationError("Passwords do not match.")
        return cleaned_data
