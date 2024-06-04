# Running Your Django App on the Development Server

To run your Django app on the development server, follow these detailed steps:

## Step 1: Navigate to Your Project Directory

Open Terminal (macOS/Linux) or Command Prompt (Windows), and navigate to your project directory. This is the directory that contains the `manage.py` file.

```bash
cd path/to/your/project
```

## Step 2: Start the Development Server
Run the following command to start the development server:

```bash
python manage.py runserver
```

By default, this will start the server at http://127.0.0.1:8000/.

## Step 3: Access Your Application
Open your web browser and go to http://127.0.0.1:8000/. You should see the default Django welcome page if everything is set up correctly.

## Step 4: Access the Admin Interface
If you have created a superuser and registered models with the admin site, you can access the admin interface at http://127.0.0.1:8000/admin/. Log in using the superuser credentials you created earlier.

## Example: Creating a Simple View
Let's create a simple view to ensure your app is working correctly.

### Step 1: Define a URL Pattern
1. Open the urls.py file in your app directory (myapp/urls.py).
2. Add the following code to define a URL pattern for your view:

```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
]
```

### Step 2: Create a View
1. Open the views.py file in your app directory (myapp/views.py).
2. Add the following code to create a simple view that returns a "Hello, World!" response:

```python
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, World!")
```

### Step 3: Include the App's URLs in the Project
Open the urls.py file in your project directory (myproject/urls.py).
Include the app's URL patterns:

```python
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('myapp.urls')),
]
```

### Step 4: Run the Development Server Again
1. Make sure your development server is running:

```bash
python manage.py runserver
```

2. Open your web browser and go to http://127.0.0.1:8000/. You should see the "Hello, World!" message.

## Conclusion
You have successfully created a simple view and run your Django app on the development server. You can now continue building your app by adding more views, models, templates, and other functionalities.
