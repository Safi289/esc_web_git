import json

from django.http import HttpResponse, JsonResponse
from .models import Company
from django.shortcuts import render


def index(request):
    companies = Company.objects.all()
    return companies





