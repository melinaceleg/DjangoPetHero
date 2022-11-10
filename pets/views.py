from django.views.generic import ListView

from pets.models import Pet


class GetAllPets(ListView):
    model = Pet
    queryset = Pet.objects.all()
    template_name = "pets/getall.html"