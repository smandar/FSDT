from django.db import models


class Users(models.Model):
    name = models.CharField(max_length=200)
    email_id = models.CharField(max_length=150)  # could have used EmailField
    mobile = models.IntegerField()
    age = models.IntegerField()
    dob = models.DateField()
    location = models.TextField()

    def __str__(self):
        return self.title
