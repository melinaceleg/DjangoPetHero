# from django.forms import forms
#
# from bookings.models import Booking
# from users.models import Availability
#
#
# class BookingForm(forms.ModelForm):
#     class Meta:
#         model = Booking
#         fields = ['availability', 'pet']
#         labels = {
#             'username': 'Username',
#             'first_name': 'First name',
#             'last_name': 'Last name',
#             'email': 'Email',
#         }
#         widgets = {
#             'availability': Availability.objects.get(forms.TextInput(attrs={'class':'form-control'})),
#             'pet': forms.TextInput(attrs={'class':'form-control'}),
#         }