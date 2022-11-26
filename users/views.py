from datetime import datetime

from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, FormView
from django.views.generic.detail import DetailView

from .models import Owner, Keeper, Availability


# Create your views here.

class GetAllOwners(ListView):
    model = Owner
    queryset = Owner.objects.all()
    template_name = "users/getall.html"

    def get_queryset(self):
        qs = super(GetAllOwners, self).get_queryset()
        for element in qs:
            if not element.__class__ == "Owner":
                qs.exclude(pk=element.pk)
        return qs

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['date'] = datetime.now()
        return context


class GetAllKeepers(ListView):
    model = Keeper
    queryset = Keeper.objects.all()
    template_name = "users/getkeepers.html"

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context["pet_size"] = self.kwargs["pet_size"]
        # Add in a QuerySet of all the books
        context['date'] = datetime.now()
        return context


# @login_required
class OwnerDetailView(LoginRequiredMixin, DetailView):
    model = Owner
    template_name = "users/detailuser.html"


class KeeperDetailView(LoginRequiredMixin, DetailView): #Poner como FormView!!!!!!!!!!!!!!!!!!!
    model = Keeper
    template_name = "users/detailkeeper.html"

    #def post(self): Y HACER EL POST!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!



# def Login(request):
#     # template_name = "users/login.html"
#     return render(request, 'users/login.html', {})

# @csrf_exempt
def Login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        # user = authenticate(request, username=username, password=password) NO FUNCIONA
        user = User.objects.get(username=username)
        # if user is not None:
        if user.password == password:
            form = login(request, user)
            return redirect(f"{user.pk}/detailUser")
        else:
            messages.add_message(request, messages.INFO, 'Please log in.')
            # return render(request, 'users/login.html', {})

    return render(request, 'users/login.html', {})
