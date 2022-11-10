from datetime import datetime

from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render
from django.views.generic import ListView
from django.views.generic.detail import DetailView

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


# @login_required
class OwnerDetailView(LoginRequiredMixin, DetailView):
    model = Owner
    template_name = "users/detailuser.html"


# def Login(request):
#     # template_name = "users/login.html"
#     return render(request, 'users/login.html', {})



def Login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            form = login(request, user)
            return redirect(f"{user.pk}/detailUser")

    return render(request, 'users/login.html', {})
