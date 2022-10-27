from datetime import datetime

from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.views.generic import ListView

from .models import Owner


# Create your views here.

class GetAllOwners(ListView):
    model = Owner
    queryset = Owner.objects.all()
    template_name = "users/getall.html"

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['date'] = datetime.now()
        return context
