# Creating Base Template

Creating a base template in Django is a common practice to ensure a consistent look and feel across your web application. A base template includes the common layout elements such as the header, footer, and navigation bar, which can be extended by other templates. Here's a step-by-step guide to creating and using a base template in Django:

### 1. Create the Base Template

First, create a directory named `templates` in your app (if it doesn’t exist). Inside this directory, create another directory with the name of your app (e.g., `myapp`). Then, create a file named `base.html` in this directory.

```
myapp/
├── templates/
│   └── myapp/
│       └── base.html
```

### 2. Define the Base Template Structure

In `base.html`, define the basic structure of your HTML document. Use `{% block %}` tags to create placeholders for content that will be overridden by child templates.

#### Example of `base.html`:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>{% block title %}My Site{% endblock %}</title>
    <link rel="stylesheet" type="text/css" href="{% static 'css/style.css' %}">
</head>
<body>
    <header>
        <h1>My Site</h1>
        <nav>
            <ul>
                <li><a href="{% url 'home' %}">Home</a></li>
                <li><a href="{% url 'about' %}">About</a></li>
                <li><a href="{% url 'contact' %}">Contact</a></li>
            </ul>
        </nav>
    </header>
    
    <div class="content">
        {% block content %}{% endblock %}
    </div>
    
    <footer>
        <p>&copy; 2024 My Site. All rights reserved.</p>
    </footer>
</body>
</html>
```

### 3. Extend the Base Template in Child Templates

Create other templates that extend the base template. These child templates will override the blocks defined in the base template.

#### Example of a Child Template (e.g., `home.html`):

1. Create `home.html` in the `templates/myapp` directory.

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>{% block title %}Home{% endblock %}</title>
</head>
<body>
    {% extends "myapp/base.html" %}

    {% block content %}
        <h2>Welcome to the Home Page!</h2>
        <p>This is the home page of my site.</p>
    {% endblock %}
</body>
</html>
```

### 4. Configure Template Settings

Ensure that Django knows where to find your templates. In `settings.py`, configure the `TEMPLATES` setting to include your app's templates directory.

```python
# settings.py
import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```

### 5. Using the Templates in Views

In your views, render the templates by passing the context data.

#### Example of a View Function:

```python
from django.shortcuts import render

def home(request):
    return render(request, 'myapp/home.html')

def about(request):
    return render(request, 'myapp/about.html')

def contact(request):
    return render(request, 'myapp/contact.html')
```

### 6. URLs Configuration

Make sure to map the views to URLs in your app’s `urls.py`.

```python
# myapp/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
]
```

### 7. Load Static Files

Ensure you load static files properly. In your base template, load the `static` template tag and reference your CSS or JavaScript files using the `{% static %}` tag.

```html
{% load static %}
<link rel="stylesheet" type="text/css" href="{% static 'myapp/css/style.css' %}">
```

### Example Directory Structure

Your project structure might look like this:

```
myproject/
├── myapp/
│   ├── templates/
│   │   └── myapp/
│   │       ├── base.html
│   │       ├── home.html
│   │       ├── about.html
│   │       └── contact.html
│   ├── static/
│   │   └── myapp/
│   │       ├── css/
│   │       │   └── style.css
│   ├── views.py
│   ├── urls.py
│   ├── models.py
│   └── ...
├── manage.py
└── myproject/
    ├── settings.py
    ├── urls.py
    └── ...
```

### Conclusion

Creating a base template in Django helps you maintain a consistent layout across your web application. By using template inheritance, you can define a common structure in the base template and extend it in child templates, ensuring DRY (Don't Repeat Yourself) principles and making your templates easier to manage and update.