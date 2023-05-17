from django.http import HttpResponse
from django.shortcuts import render
from django.http import JsonResponse
import random


# def index(request):
#     return HttpResponse("Hello, world. You're at the polls index.")


def index(request):
    # Pass the value to the template
    return render(request, 'dynamic_value.html')
