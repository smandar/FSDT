from django.db import models
# from django.forms import ModelForm
from django.utils import timezone


class Contacts(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=150, blank=True)
    last_name = models.CharField(max_length=150, blank=True)
    email_id = models.EmailField(max_length=150)  # could have used EmailField
    mobile = models.CharField(max_length=15)
    age = models.IntegerField()
    dob = models.DateField()
    location = models.TextField(default='Not available')
    last_dml_time = models.DateTimeField(default=timezone.now)


    def __str__(self):
        return self.first_name


# class addContactsForm(ModelForm):
#     class Meta:
#         model= Contacts
#         fields =['name', 'email_id', 'mobile', 'age','dob','location']
