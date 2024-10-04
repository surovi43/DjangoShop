from django.http import JsonResponse
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate, login as signIn, logout as signOut
from .forms import UserRegistrationForm, UserSignInForm

User = get_user_model()


def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            # Create a new user
            name = f"{form.cleaned_data.get("fname")} {form.cleaned_data.get("lname")}"
            email = form.cleaned_data.get("email")
            password = form.cleaned_data.get("password")
            User.objects.create_user(name=name, email=email, password=password)

            # Automatically log in the user
            user = authenticate(request, email=email, password=password)
            signIn(request, user)
            messages.success(request, "Account created successfully!")

            return redirect("home")
    else:
        form = UserRegistrationForm()

    return render(request, "register.html", {"form": form})


def login(request):
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
    signOut(request)
    return JsonResponse({"message": "Logged out successfully"}, status=200)
