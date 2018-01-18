
     ,-----.,--.                  ,--. ,---.   ,--.,------.  ,------.
    '  .--./|  | ,---. ,--.,--. ,-|  || o   \  |  ||  .-.  \ |  .---'
    |  |    |  || .-. ||  ||  |' .-. |`..'  |  |  ||  |  \  :|  `--,
    '  '--'\|  |' '-' ''  ''  '\ `-' | .'  /   |  ||  '--'  /|  `---.
     `-----'`--' `---'  `----'  `---'  `--'    `--'`-------' `------'
    -----------------------------------------------------------------


<h1> ConnectDoc </h1>

This Ecommerce & Blog Web Application was built as a final project for the Code Institute's classroom bootcamp. The project is aimed at allowing patients looking for various medical services to search online, pick and book appointments with their preferred clinics or doctors in their area.

This is a fictional Ecommerce site built with Python's Django framework.

<h2> How does it work? </h2>
ConnectDoc is a Django project built with Multiple User Authentication and Stripe Payments.
The search function will compare the result you are searching for with what you already have in your collection (signed up doctors and clinics). It will then use either clinic, doctor or location as a search parameter and when querying it will loop through the existing database entries and check for matches.


<h2> Live Demo </h2>
Follow this link to view the deployed version of the web app https://stream3project.herokuapp.com/

<h2> Built with: </h2>

Django framework
Python
HTML
CSS
Bootstrap
SQLite database



<h2> URL's </h2>
urls.py at the project level (ConnectDoc) gives the url patterns, routes to views, either directly:

from django.conf.urls import url, include
from .views import practice_details, all_docs
from booking.views import booking
from checkout import urls as checkout_urls

urlpatterns = [
    url(r'^$', all_docs, name='all_docs'),
    # url(r'^$', all_doctors, name='medicalPractice'),
    url(r'^(\d+)$', practice_details, name='practice_details'),
    url(r'^(\d+)/booking$', booking, name='booking'),
    url(r'^(\d+)/booking/checkout', include(checkout_urls)),
]


Or for the Apps that have their own urls, via the 'include' function:

from accounts import urls as accounts_urls

urlpatterns = [url(r'^accounts/', include(accounts_urls))]




<h2> Views </h2>
Views called via URLs are Python functions that perform the different actions required to make the Website function e.g. render a template, log someone in, log them out etc.

<h2> Templates </h2>
The base.html page in the top-level templates folder is the base template used for all pages and includes all the links CSS/Bootstrap/Javascript etc. and the fully responsive navbar and footer that appears on all pages of the Website. It also contains:

{% block content %}
{% endblock content %}
Which allows other templates to be inserted in to that section (between the navbar & footer). Linking the base.html to templates within Apps:

{% extends 'base.html' %}

{% block content %}

All code for the app goes in here & will appear between the navbar & footer from base.html

{% endblock content %}

<h2> Apps </h2>

<h4> ConnectDoc </h4>
ConnectDoc is the Home App which renders the index.html template, which in turn calls the base.html template to present a full webpage with navbar, content and footer.

<h4> Search </h4>
The Search App uses a simple Python function to search through all the doctors, clinics or also doctors within clinics & render the results.html page which displays them.

<h4> Accounts </h4>
The Accounts App is used for the complete MULTIPLE users authentication. When users first visit the website they have the option to either Register or Log In. If the user has no account, there is the option to register either as a Patient, Doctor or Medical practice, each choice having its individual customised registration form, or simply Log in if they already have an account. Once Registered/Logged in they can view their own profile that will display their username and email address they used to register with. The two options under 'My Account' will then change to Profile or Log Out. Once logged in, users will be able to book an appointment with their preferred clinic or doctor and once the submit booking button is clicked, a function is called within the views.py in the Booking App which will connect users with Stripe payments if the client is logged in and if the card details are entered correctly into the form it will take a monthly payment from the user.

<h4> Clinics </h4>
This App searches through all the Clinics that have been added via Django's admin panel or via direct registration. In the navbar there is the option to search only for Clinics by clicking on the Clinics button which will render the practice_detail.html file and all the registered clinics will be displayed. Following this, once a specific clinic is selected from the list generated, this will load a new page that will list all the doctors registered with that specific clinic. After the doctor is selected, the full profile of the doctor is shown in a new page which also contains the button to proceed with booking the actual appointment on the selected date and time.

<h4> Medical Practice </h4>
This App searches through all Doctors that have been added via Django's admin panel or via direct registration. Doctors will have to pick an existing clinic to register themselves with when creating an account. In the navbar there is the option to search only for Doctors. By clicking on Doctors, the all_docs.html will be rendered.

<h4> Booking </h4>
This App takes the doctor ID and if the user is logged in, proceeds to take the date and time selection of the appointment and checkout to finalise with the payment.

<h4> Payments/Checkout </h4>
The Checkout App stores the booking time/date and price of the appointment with the selected doctor and displays a basket total. The Checkout App then renders a form for a one-off Stripe payment.


<h2> Deployment / Hosting </h2>
This Project was deployed and is hosted on Heroku with automatic deploys from GitHub

<h2> Databases / Static Files </h2>
When running locally, SQLite database was used & static and media files were stored locally. When deploying, Heroku Postgres was used as the server database & an Amazon S3 bucket was set up to host all the static files. settings.py file was amended for the database & static files to point to the online resources.

<h2> Installation </h2>
Follow the below instructions to clone this project for Mac (commands will be slightly different for Windows)

Go to folder you want to put the cloned project in your terminal & type: $ git clone https://github.com/cozmaoanna/connectDoc
Create & Activate a new Virtual Environment in terminal: Create: $ python3 -m venv ~/virtualenvs/name_of_environment Activate: $ source ~/virtualenvs/name_of_environment/bin/activate
Install the project dependancies: $ pip install -r requirements.txt
Create env.sh file at the top level (this will contain all sensitive information) MAKE SURE IT IS IN THE .gitignore FILE
Copy the following into the env.sh file:
#!/bin/sh

export SECRET_KEY=''
export DEBUG='True'

export STRIPE_PUBLISHABLE_KEY=''
export STRIPE_SECRET_KEY=''

export EMAIL_HOST_USER='your@gmail.com'
export EMAIL_HOST_PASSWORD='yourPassword'
A new SECRET_KEY can be generated here
Set up an account with Stripe here & input STRIPE_PUBLISHABLE_KEY & STRIPE_SECRET_KEY
Create email address with gmail & input your credentials
Go to settings.py, change the following(lines 177-205):

TO RUN LOCALLY HAVE THESE TWO UNCOMMENTED:

 STATIC_URL = '/static/'
 MEDIA_URL = '/media/'


 TO RUN ON HEROKU HAVE THESE UNCOMMENTED:

AWS_HEADERS = {  # see http://developer.yahoo.com/performance/rules.html#expires
        'Expires': 'Thu, 31 Dec 2099 20:00:00 GMT',
        'Cache-Control': 'max-age=94608000',
    }


AWS_STORAGE_BUCKET_NAME = os.environ.get('BUCKET_NAME')
AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY')
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')

AWS_S3_HOST = 's3-eu-west-1.amazonaws.com'
AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME


STATICFILES_LOCATION = 'static'
STATICFILES_STORAGE = 'custom_storages.StaticStorage'
STATIC_URL = "https://%s/%s/" % (AWS_S3_CUSTOM_DOMAIN, STATICFILES_LOCATION)

MEDIAFILES_LOCATION = 'media'
MEDIA_URL = "https://%s/%s/" % (AWS_S3_CUSTOM_DOMAIN, MEDIAFILES_LOCATION)
DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'
To this:

 TO RUN LOCALLY HAVE THESE TWO UNCOMMENTED

STATIC_URL = '/static/'
MEDIA_URL = '/media/'


 TO RUN ON HEROKU HAVE THESE UNCOMMENTED

 AWS_HEADERS = {  # see http://developer.yahoo.com/performance/rules.html#expires
        'Expires': 'Thu, 31 Dec 2099 20:00:00 GMT',
         'Cache-Control': 'max-age=94608000',
     }


 AWS_STORAGE_BUCKET_NAME = os.environ.get('BUCKET_NAME')
 AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY')
 AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')

 AWS_S3_HOST = 's3-eu-west-1.amazonaws.com'
 AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME


 STATICFILES_LOCATION = 'static'
 STATICFILES_STORAGE = 'custom_storages.StaticStorage'
 STATIC_URL = "https://%s/%s/" % (AWS_S3_CUSTOM_DOMAIN, STATICFILES_LOCATION)

 MEDIAFILES_LOCATION = 'media'
 MEDIA_URL = "https://%s/%s/" % (AWS_S3_CUSTOM_DOMAIN, MEDIAFILES_LOCATION)
 DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'
Also in settings.py change the following(lines 112-119):
 DATABASES = {
     'default': {
         'ENGINE': 'django.db.backends.sqlite3',
         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
     }
 }

DATABASES = {'default': dj_database_url.parse(os.environ.get('DATABASE_URL')) }
To this:

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

 DATABASES = {'default': dj_database_url.parse(os.environ.get('DATABASE_URL')) }
In the terminal: $ python manage.py migrate - this will apply migrations to your local sqlite database $ python manage.py createsuperuser - this will create admin support $ python manage.py runserver -  starting development server.

<h2> Running the tests </h2>
Automated tests can be viewed in the tests.py file within the separate Apps. To run the tests, in your terminal navigate to the folder with your project in, activate your virtual environment and type:

$ python manage.py test <app name>

$ python manage.py test accounts - These will all PASS tests.py n the Accounts App:

Tests that the UserRegistrationForm validates properly when the correct information is supplied
Tests that the form fails when one of the passwords has not been entered
Tests that the form fails when the passwords to not match

$ python3 manage.py test search - This will PASS tests.py in the Search App:
Tests that the url for '/search/' resolves to the 'do_search' function in views.py
