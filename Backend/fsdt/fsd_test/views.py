from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponseRedirect
from .models import Contacts
from datetime import datetime
from django.utils import timezone
from django.http import HttpResponse
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

        ip_fname = request.POST.get('first_name')
        ip_lname = request.POST.get('last_name')
        ip_user_email = request.POST.get('user_email')
        ip_phone = request.POST.get('phone')
        ip_age = request.POST.get('age')
        ip_DoB = request.POST.get('DoB')
        ip_location = request.POST.get('location')

        ip_DoB = datetime.strptime(ip_DoB, '%d/%m/%Y').strftime('%Y-%m-%d')
        print ip_DoB

        # initcap name

        contact = Contacts(first_name=ip_fname.lower().title(),
                last_name=ip_lname.lower().title(),
                email_id=ip_user_email,
                mobile=ip_phone,
                age=ip_age,
                dob=ip_DoB,
                location=ip_location)

        print contact
        contact.save()

        response_data = {}
        response_data['result'] = 'Post successful!'
        response_data['contact_id'] = contact.id
        response_data['name'] = contact.first_name + contact.last_name
        response_data['created'] = contact.last_dml_time.strftime(
            '%B %d, %Y %I:%M %p')

        return HttpResponse(
            json.dumps(response_data),
            content_type="application/json"
        )

    else:
        return HttpResponse(
            json.dumps({"nothing to see": "this isn't happening"}),
            content_type="application/json"
        )

def update_contact(request):
    if request.method == 'POST':

        ip_id = request.POST.get('id')
        ip_fname = request.POST.get('first_name')
        ip_lname = request.POST.get('last_name')
        ip_user_email = request.POST.get('user_email')
        ip_phone = request.POST.get('phone')
        ip_age = request.POST.get('age')
        ip_DoB = request.POST.get('DoB')
        ip_location = request.POST.get('location')

        ip_DoB = datetime.strptime(ip_DoB, '%d/%m/%Y').strftime('%Y-%m-%d')
        print ip_DoB

        # initcap name
        mod_contact = Contacts.objects.get(id=ip_id)
        mod_contact.first_name = ip_fname.lower().title()
        mod_contact.last_name = ip_lname.lower().title()
        mod_contact.email_id = ip_user_email
        mod_contact.mobile = ip_phone
        mod_contact.age = ip_age
        mod_contact.dob = ip_DoB
        mod_contact.location = ip_location
        mod_contact.last_dml_time =datetime.now()
        print mod_contact.last_dml_time
        mod_contact.save()

        response_data = {}
        response_data['result'] = 'Update successful!'
        response_data['contact_id'] = mod_contact.id
        response_data['name'] = mod_contact.first_name + mod_contact.last_name
        response_data['created'] = mod_contact.last_dml_time.strftime(
            '%B %d, %Y %I:%M %p')

        return HttpResponse(
            json.dumps(response_data),
            content_type="application/json"
        )

    else:
        return HttpResponse(
            json.dumps({"nothing to see": "this isn't happening"}),
            content_type="application/json"
        )
