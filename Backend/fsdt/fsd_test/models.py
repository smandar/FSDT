from django.db import models
from django.forms import ModelForm
from django.utils import timezone


class Contacts(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    email_id = models.EmailField(max_length=150)  # could have used EmailField
    mobile = models.BigIntegerField()
    age = models.IntegerField()
    dob = models.DateField()
    location = models.TextField(default='Not available')
    last_dml_time = models.DateTimeField(default=timezone.now)


    def __str__(self):
        return self.name


class addContactsForm(ModelForm):
    class Meta:
        model= Contacts
        fields =['name', 'email_id', 'mobile', 'age','dob','location']
