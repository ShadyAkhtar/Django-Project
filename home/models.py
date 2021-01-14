from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length = 122)
    email = models.CharField(max_length = 122)
    phone = models.CharField(max_length = 12)
    desc = models.TextField()
    date = models.DateField()

    #How you want to see the object in database heading (display title) for entry
    def __str__(self):
        return self.name + " " + "-" + " "  + self.email