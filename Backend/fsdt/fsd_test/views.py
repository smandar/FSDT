from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Contacts
from .models import addContactsForm
# from fsd_test.forms import addContactsForm
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


def create_contact(request):
    if request.method == 'POST':
        f = addContactsForm(request.POST)
        if f.is_valid():
            new_contact = f.save()
        # form_name = request.POST.get('name')
            output_data = {}
        # print name

        # new_contacts = Contacts(name=form_name)
        # new_contacts.save(commit=True)

            output_data['result'] = 'Details entered successfully'
        # response_data['name'] = new_contacts.name

            return HttpResponse(
                json.dumps(output_data),
                content_type="application/json"
            )
    else:
        return HttpResponse(
            json.dumps({"nothing to see": "this isn't happening"}),
            content_type="application/json"
        )

    return HttpResponseRedirect(view.listing)

