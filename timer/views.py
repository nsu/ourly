# Create your views here.

from .models import WorkSession
from .forms import WorkSessionForm
from django.shortcuts import render, HttpResponseRedirect
from datetime import datetime


def clockin(request):
    pass
