from django import forms
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model, authenticate
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth.password_validation import password_validators_help_texts

User = get_user_model()


class BaseUserForm(forms.ModelForm):
    """Base form to handle common functionalities for User forms."""

    def clean_required_fields(self, field_name, label):
        """Helper method to validate required fields."""
        value = self.cleaned_data.get(field_name)
        if not value:
            raise ValidationError(f"{label} is required.")
        return value


class UserRegistrationForm(BaseUserForm):
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
        help_text=" ".join(password_validators_help_texts()),
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
        validate_password(password)
        return password

    def clean_confirm_password(self):
        return self.clean_required_fields("confirm_password", label="Confirm password")

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password and confirm_password and password != confirm_password:
            raise ValidationError("Passwords do not match.")
        return cleaned_data


class UserSignInForm(BaseUserForm):
    email = forms.EmailField(
        label="Email",
        widget=forms.EmailInput(
            attrs={
                "class": "input w-full px-10",
                "placeholder": "Enter your email",
                "autocomplete": "email",
            }
        ),
    )
    password = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(
            attrs={
                "class": "password-field w-full px-10",
                "placeholder": "Enter a password",
            }
        ),
    )

    class Meta:
        model = User
        fields = ["email", "password"]

    def clean_email(self):
        email = self.clean_required_fields("email", label="Email")
        return email

    def clean_password(self):
        password = self.clean_required_fields("password", label="Password")
        return password

    def clean(self):
        """Authenticate the user"""
        cleaned_data = super().clean()
        email = cleaned_data.get("email")
        password = cleaned_data.get("password")

        # Check if a user exists with the given email
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            raise ValidationError(
                "No user exists with the provided email.", code="invalid_email"
            )

        # Check if the password matches
        if not user.check_password(password):
            raise ValidationError(
                "The password you entered is incorrect.", code="invalid_password"
            )

        # If both email and password are correct, authenticate the user
        user = authenticate(email=email, password=password)

        if not user:
            raise ValidationError("Authentication failed.", code="invalid_login")

        self.cleaned_data["user"] = user
        return cleaned_data
