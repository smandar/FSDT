from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponseRedirect
from .models import Contacts
from .models import addContactsForm
from datetime import datetime
from django.http import HttpResponse
from django.forms import ModelForm
import json

# Create your views here.


def listing(request):
    contacts = Contacts.objects.all()
    return render(request, 'frontend/listing.html', {'contacts': contacts})

# can add the update/ add parameter here!


def modify(request):
    return render(request, 'frontend/modify.html', {})

# learn ModelForm

def create_contact(request):
    if request.method == 'POST':

        ip_name = request.POST.get('name')
        ip_user_email = request.POST.get('user_email')
        ip_phone = request.POST.get('phone')
        ip_age = request.POST.get('age')
        ip_DoB = request.POST.get('DoB')
        ip_location = request.POST.get('location')

        ip_DoB = datetime.strptime(ip_DoB, '%d/%m/%Y').strftime('%Y-%m-%d')
        print ip_DoB

        contact = Contacts(name=ip_name,email_id=ip_user_email,mobile=ip_phone
                           ,age=ip_age,dob=ip_DoB,location=ip_location)
        print contact
        contact.save()

        response_data ={}
        response_data['result'] = 'Post successful!'
        response_data['contact_id'] = contact.id
        response_data['name'] = contact.name
        response_data['created'] = contact.last_dml_time.strftime('%B %d, %Y %I:%M %p')


        return HttpResponse(
            json.dumps(response_data),
            content_type="application/json"
        )
    else:
        return HttpResponse(
            json.dumps({"nothing to see": "this isn't happening"}),
            content_type="application/json"
        )

