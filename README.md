
     ,-----.,--.                  ,--. ,---.   ,--.,------.  ,------.
    '  .--./|  | ,---. ,--.,--. ,-|  || o   \  |  ||  .-.  \ |  .---'
    |  |    |  || .-. ||  ||  |' .-. |`..'  |  |  ||  |  \  :|  `--,
    '  '--'\|  |' '-' ''  ''  '\ `-' | .'  /   |  ||  '--'  /|  `---.
     `-----'`--' `---'  `----'  `---'  `--'    `--'`-------' `------'
    -----------------------------------------------------------------


ConnectDoc

This Ecommerce & Blog Web Application was built as a final project for the Code Institute's classroom bootcamp. The project is aimed at allowing patients looking for various medical services to search online, pick and book appointments with their preferred clinics or doctors in their area.

This is a fictional Ecommerce site built with Python's Django framework.

How does it work?
ConnectDoc is a Django project built with Multiple User Authentication and Stripe Payments.
The search function will compare the result you are searching for with what you already have in your collection (signed up doctors and clinics). It will then use either clinic, doctor or location as a search parameter and when querying it will loop through the existing database entries and check for matches.


Live Demo
Follow this link to view the deployed version of the web app https://dashboard.heroku.com/apps/stream3project

Built with:
Django framework
Python
HTML
CSS
Bootstrap
SQLite database



URL's
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




Views
Views called via URLs are Python functions that perform the different actions required to make the Website function e.g. render a template, log someone in, log them out etc.

Templates
The base.html page in the top-level templates folder is the base template used for all pages and includes all the links CSS/Bootstrap/Javascript etc. and the fully responsive navbar and footer that appears on all pages of the Website. It also contains:

{% block content %}
{% endblock content %}
Which allows other templates to be inserted in to that section (between the navbar & footer). Linking the base.html to templates within Apps:

{% extends 'base.html' %}

{% block content %}

All code for the app goes in here & will appear between the navbar & footer from base.html

{% endblock content %}

Apps

ConnectDoc
ConnectDoc is the Home App which renders the index.html template, which in turn calls the base.html template to present a full webpage with navbar, content and footer.

Search
The Search App uses a simple Python function to search through all the doctors, clinics or also doctors within clinics & render the results.html page which displays them.

Accounts
The Accounts App is used for the complete MULTIPLE users authentication. When users first visit the website they have the option to either Register or Log In. If the user has no account, there is the option to register either as a Patient, Doctor or Medical practice, each choice having its individual customised registration form, or simply Log in if they already have an account. Once Registered/Logged in they can view their own profile that will display their username and email address they used to register with. The two options under 'My Account' will then change to Profile or Log Out. Once logged in, users will be able to book an appointment with their preferred clinic or doctor and once the submit booking button is clicked, a function is called within the views.py in the Booking App which will connect users with Stripe payments if the client is logged in and if the card details are entered correctly into the form it will take a monthly payment from the user.

Clinics
This App searches through all the Clinics that have been added via Django's admin panel or via direct registration. In the navbar there is the option to search only for Clinics by clicking on the Clinics button which will render the practice_detail.html file and all the registered clinics will be displayed. Following this, once a specific clinic is selected from the list generated, this will load a new page that will list all the doctors registered with that specific clinic. After the doctor is selected, the full profile of the doctor is shown in a new page which also contains the button to proceed with booking the actual appointment on the selected date and time.

Medical Practice
This App searches through all Doctors that have been added via Django's admin panel or via direct registration. Doctors will have to pick an existing clinic to register themselves with when creating an account. In the navbar there is the option to search only for Doctors. By clicking on Doctors, the all_docs.html will be rendered.

Booking
This App takes the doctor ID and if the user is logged in, proceeds to take the date and time selection of the appointment and checkout to finalise with the payment.

Payments/Checkout
The Checkout App stores the booking time/date and price of the appointment with the selected doctor and displays a basket total. The Checkout App then renders a form for a one-off Stripe payment.


Deployment / Hosting
This Project was deployed and is hosted on Heroku with automatic deploys from GitHub

Databases / Static Files
When running locally, SQLite database was used & static and media files were stored locally. When deploying, Heroku Postgres was used as the server database & an Amazon S3 bucket was set up to host all the static files. settings.py file was amended for the database & static files to point to the online resources.

Installation
Follow the below instructions to clone this project for Mac (commands will be slightly different for Windows)

Go to folder you want to put the cloned project in your terminal & type: $ git clone https://github.com/kgmaxwell1990/urban-surf.git
Create & Activate a new Virtual Environment in terminal: Create: $ python3 -m venv ~/virtualenvs/name_of_environment Activate: $ source ~/virtualenvs/name_of_environment/bin/activate
Install the project dependancies: $ pip install -r requirements.txt
Create env.sh file at the top level (this will contain all sensitive information) MAKE SURE IT IS IN THE .gitignore FILE
Copy the following into the env.sh file:
#!/bin/sh

export SECRET_KEY=''
export DEBUG='True'

export STRIPE_PUBLISHABLE_KEY=''
export STRIPE_SECRET_KEY=''

<!--export EMAIL_HOST_USER='your@gmail.com'-->
<!--export EMAIL_HOST_PASSWORD='yourPassword'-->
A new SECRET_KEY can be generated here
Set up an account with Stripe here & input STRIPE_PUBLISHABLE_KEY & STRIPE_SECRET_KEY
Create email address with gmail & input your credentials
Go to settings.py, change the following(lines 177-205):
# TO RUN LOCALLY HAVE THESE TWO UNCOMMENTED #

# STATIC_URL = '/static/'
# MEDIA_URL = '/media/'


# TO RUN ON HEROKU HAVE THESE UNCOMMENTED #

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

# TO RUN LOCALLY HAVE THESE TWO UNCOMMENTED #

STATIC_URL = '/static/'
MEDIA_URL = '/media/'


# TO RUN ON HEROKU HAVE THESE UNCOMMENTED #

# AWS_HEADERS = {  # see http://developer.yahoo.com/performance/rules.html#expires
#         'Expires': 'Thu, 31 Dec 2099 20:00:00 GMT',
#         'Cache-Control': 'max-age=94608000',
#     }


# AWS_STORAGE_BUCKET_NAME = os.environ.get('BUCKET_NAME')
# AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY')
# AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')

# AWS_S3_HOST = 's3-eu-west-1.amazonaws.com'
# AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME


# STATICFILES_LOCATION = 'static'
# STATICFILES_STORAGE = 'custom_storages.StaticStorage'
# STATIC_URL = "https://%s/%s/" % (AWS_S3_CUSTOM_DOMAIN, STATICFILES_LOCATION)

# MEDIAFILES_LOCATION = 'media'
# MEDIA_URL = "https://%s/%s/" % (AWS_S3_CUSTOM_DOMAIN, MEDIAFILES_LOCATION)
# DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'
Also in settings.py change the following(lines 112-119):
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }

DATABASES = {'default': dj_database_url.parse(os.environ.get('DATABASE_URL')) }
To this:

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# DATABASES = {'default': dj_database_url.parse(os.environ.get('DATABASE_URL')) }
In the terminal: $ python manage.py migrate - this will apply migrations to your local sqlite database $ python manage.py createsuperuser - this will create admin support $ python manage.py runserver - should say starting development server..
Go to your browser & type '127.0.0.1:8000' in the address bar
The App should run on your browser - note that there will be no products/blog posts as you are running off your own blank database
Log in to the admin panel by going to '127.0.0.1:8000/admin' & log in using the credentials you created for the superuser
You can add products/categories & blog posts from here
Running the tests
Automated tests can be viewed in the tests.py file within the separate Apps. To run the tests, in your terminal navigate to the folder with your project in, activate your virtual environment and type:

$ python manage.py test <app name>

$ python manage.py test accounts - These will all PASS tests.py n the Accounts App:

Tests that the UserRegistrationForm validates properly when the correct information is supplied
Tests that the form fails when one of the passwords has not been entered
Tests that the form fails when the passwords to not match
<!--$ python manage.py test cart - This will PASS tests.py in the Cart App:-->

<!--Tests that the url for '/cart/' resolves to the 'cart' function in views.py-->
<!--$ python manage.py test contact - These will both PASS tests.py in the Contact App:-->

<!--Tests that the url for '/contact/' resolves to the 'contact' function in views.py-->
<!--Tests that the view returns the correct status code-->
<!--etc. etc.-->