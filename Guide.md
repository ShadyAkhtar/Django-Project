# Steps for Django Project
# To install Django, make sure u have the path in environmental variable

C:\Users\shady\AppData\Local\Programs\Python\Python38-32
C:\Users\shady\AppData\Local\Programs\Python\Python38-32\Scripts

## Install Django by running this command on powershell
- pip install Django

- django-admin

## To create a project  
- django-admin startproject mysite

## To start the server
- python manage.py runserver

**Where mysite is a site name**

cd mysite (open vscode here in mysite folder)

## Make migratation

- python manage.py makemigrations

- python manage.py migrate

## create app

- python manage.py startapp home (create app 'home')

## create static folder

## create template folder

> **set the path of static and template dir in settings.py**

![Static Dirs](static/screenshots/static-dirs.png?raw=true "Static Dirs")

![template Dirs](static/screenshots/template-dirs.png?raw=true "template Dirs")

## create superuser for db

python manage.py createsuperuser


## unique token for form submission

 {% csrf_token %}

 (check contact.html)
 

## to save the form in database we have to define the model in 
> home/models.py

## after that we have to migrate

- python manage.py makemigrations

## to make migration first register the models we created  
> home/admin.py

- from home.models import Contact
- admin.site.register(Contact)

![register model](static/screenshots/register-model.png?raw=true "Register Model")

## go to - 
> home/apps.py

**copy the name of the apps i.e. name of the class exist in apps.py**

- HomeConfig

![App Name](static/screenshots/app-name.png?raw=true "App Name")

- and paste it in settings.py (one previous directory)

**paste under :**

INSTALLED_APPS = [
'home.apps.HomeConfig',
.
.
.]

![Setting Installed Apps](static/screenshots/settings-installed-apps.png?raw=true "Setting Installed Apps")

## Now Migrate 
- python manage.py makemigrations
- python manage.py migrate

## Now create a post request in 
> home/views.py

**import :**
- from home.models import Contact
- from datetime import datetime

**under contact(request) method**
if request.method == "POST":
    name = request.POST.get('name')
    email = request.POST.get('email')
    phone = request.POST.get('phone')
    desc = request.POST.get('desc')
    contact = Contact(name=name, email=email, phone=phone, desc=desc, date=datetime.today())
    contact.save()

## Check the django admin for saved data

## create alert on successful message submission

**paste it in settings.py**

**under import os**
- from django.contrib.messages import constants as messages

**paste in views.py**

- from django.contrib import messages
under contact(request) function
after contact.save()
- messages.success(request, 'your message has been sent!')

> write alert popup code in contact.html

## Python shell for django

- python manage.py shell

**to view all objects in Contact**

- Contact.objects.all()
- Contact.objects.all().first()
- Contact.objects.all().last()
- Contact.objects.all()[0] (to check Contacts Attribute)
- Contact.objects.all()[1]
- Contact.objects.all()[0].name (ut will display the value of name)
- Contact.objects.all()[0].email

 **Search**
- Contact.objects.filter(name="shadab")
- Contact.objects.filter(name="shadab", phone="9167937391")

**make changes to object**
- ins = Contact.objects.filter(name="shadab", phone="9167937391")[0]
- ins.phone = "9632587410"
- ins.save()

- Contact.objects.filter(desc__startswith="hey")

- exit()

## refer making queries in django official webpage
[here]https://docs.djangoproject.com/en/3.1/topics/db/queries/
