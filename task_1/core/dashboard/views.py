from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from app.models import *


@login_required
def dashboard(request):
    template = 'admin/dashboard/dashboard.html'

    return render(request, template, {})