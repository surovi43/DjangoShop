"""
This module contains views functions for different pages of the website.
"""

from django.http import HttpResponse
from django.shortcuts import render


def homepage(request):
    """View function for the homepage"""
    if request.user.is_authenticated:
        return render(request, "homepage.html", {"message": "You are logged in!"})
    else:
        return render(request, "homepage.html", {"message": "You are not logged in!"})


def about(request):
    """View function for the about page"""
    return HttpResponse("About page")
