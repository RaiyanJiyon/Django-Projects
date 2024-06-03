# How to Create & Setup a Django Project

Creating and setting up a Django project involves several steps. Below are the detailed instructions:

## Step 1: Install Django

Ensure you have Django installed. If not, install it using pip:

```bash
pip install django
```

## Step 2: Create a Django Project
1. Open Terminal (macOS/Linux) or Command Prompt (Windows).
2. Navigate to the directory where you want to create your project.
3. Run the following command to create a new Django project:

```bash
django-admin startproject myproject
```

Replace `myproject` with the name of your project. This command creates a new directory named myproject with the following structure:

```bash
myproject/
    manage.py
    myproject/
        __init__.py
        settings.py
        urls.py
        wsgi.py
```

## Step 3: Navigate to the Project Directory
Navigate into your project directory:

```bash
cd myproject
```

## Step 4: Run the Development Server
To verify that your project is set up correctly, start the development server:

```bash
python manage.py runserver
```

Open a web browser and go to http://127.0.0.1:8000/. You should see the Django welcome page.

## Step 5: Create a Django App
A Django project can contain multiple apps. To create an app, run the following command inside your project directory:

```bash
python manage.py startapp myapp
```

Replace myapp with the name of your app. This command creates a new directory named myapp with the following structure:

```bash
myapp/
    __init__.py
    admin.py
    apps.py
    migrations/
        __init__.py
    models.py
    tests.py
    views.py
```

## Step 6: Register the App in the Project
Open the settings.py file located in the myproject directory.
Add your app to the INSTALLED_APPS list:

```python
INSTALLED_APPS = [
    # Django apps...
    'myapp',
]
```

## Step 7: Create Models
Open the models.py file in your app directory (`myapp/models.py`).
Define your models as Python classes. For example:

```python
from django.db import models

class MyModel(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
```

## Step 8: Create Database Migrations
1. Run the following command to create migration files for your models:

```bash
python manage.py makemigrations
```

2. Apply the migrations to create database tables:

```bash
python manage.py migrate
```

## Step 9: Create an Admin User
To access the Django admin interface, you need to create a superuser:

```bash
python manage.py createsuperuser
```

Follow the prompts to set up the superuser credentials.

## Step 10: Run the Development Server
Start the development server again:

```bash
python manage.py runserver
```

You can now access the admin interface at http://127.0.0.1:8000/admin/ and log in using the superuser credentials you created.

### Conclusion
You have successfully created and set up a Django project and app. You can now start building your application's functionality.
