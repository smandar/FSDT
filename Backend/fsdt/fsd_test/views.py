from django.shortcuts import render
from .models import Contacts

# Create your views here.


def listing(request):
    contacts = Contacts.objects.order_by('-dob')
    return render(request, 'frontend/listing.html', {'contacts': contacts})

# can add the update/ add parameter here!

def modify(request):
    return render(request, 'frontend/modify.html', {})
