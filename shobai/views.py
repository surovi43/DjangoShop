"""
This module contains views functions for different pages of the website.
"""

from django.http import HttpResponse
from django.shortcuts import render


def homepage(request):
    """View function for the homepage"""
    return render(request, "homepage.html")


def about(request):
    """View function for the about page"""
    return HttpResponse("About page")
