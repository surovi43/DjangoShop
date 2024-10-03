from django.shortcuts import render, redirect
from .forms import UserRegistrationForm
from django.contrib.auth import get_user_model

User = get_user_model()


def login(request):
    return render(request, "login.html")


def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            name = f"{form.cleaned_data.get("fname")} {form.cleaned_data.get("lname")}"
            email = form.cleaned_data.get("email")
            password = form.cleaned_data.get("password")

            User.objects.create_user(name=name, email=email, password=password)
            return redirect("login")
        else:
            print(form.errors)
            return render(request, "register.html", {"form": form})

    else:
        form = UserRegistrationForm()

    return render(request, "register.html", {"form": form})
