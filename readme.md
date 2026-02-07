to start a new project:

django-admin startproject <project-name> 

cd <project-name>

python manage.py startapp <app-name>

# put the app-name in the settings file under installed apps section


to start the server:

python manage.py runserver



Note:
    To use django rest framework:
        pip install djangorestframework


    To use a custom user model:
        add the following line at the bottom of the settings file:
            AUTH_USER_MODEL = 'users.customuser'
            (you can replace customuser with your own model name)