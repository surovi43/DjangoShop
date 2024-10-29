from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as signIn, logout as signOut
from .forms import UserRegistrationForm, UserSignInForm, BecomeMerchantForm


def register(request):
    """
    This view handles the registration of a new user.
    """
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            # Save the user and set the password correctly
            user = form.save(commit=False)
            user.set_password(form.cleaned_data.get("password"))
            user.save()

            # Automatically log in the user
            user = authenticate(
                request, email=user.email, password=form.cleaned_data.get("password")
            )
            if user:
                signIn(request, user)
                messages.success(request, "Account created successfully!")
                return redirect("home")
    else:
        form = UserRegistrationForm()

    return render(request, "register.html", {"form": form})


def login(request):
    """
    This view handles the login of a user.
    """
    if request.method == "POST":
        form = UserSignInForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get("email")
            password = form.cleaned_data.get("password")
            user = authenticate(request, email=email, password=password)

            if user is not None:
                signIn(request, user)
                messages.success(request, "Successfully logged in!")
                return redirect("home")
            else:
                messages.error(request, "Invalid email or password.")
    else:
        form = UserSignInForm()

    return render(request, "login.html", {"form": form})


def logout(request):
    """
    This handles the logout of a user.
    """
    signOut(request)
    return redirect("home")


def become_merchant(request):
    """
    This view handles the login of a user.
    """
    if request.method == "POST":
        form = BecomeMerchantForm(request.POST)

        if form.is_valid():
            application = form.save(commit=True)
            if application is not None:
                messages.success(request, "Successfully submitted!")
                return redirect("home")
            else:
                messages.error(request, "Request Failed!")
        else:
            print(form.errors)

    else:
        form = BecomeMerchantForm()

    return render(request, "become_merchant.html", {"form": form})
