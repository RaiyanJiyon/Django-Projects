# Django Template Language

Django Template Language (DTL) is a powerful templating engine used to render HTML dynamically. It allows you to use various constructs like variables, filters, tags, and template inheritance to create dynamic web pages. Here’s a comprehensive guide to the Django Template Language:

## 1. Template Variables
Template variables are placeholders that you define in your views and pass to the template context. They are enclosed in double curly braces {{ }} and replaced with the variable's value when the template is rendered.

Example:

```python
<p>Hello, {{ name }}!</p>
```

## 2. Template Tags
Template tags provide arbitrary logic in the rendering process. They are enclosed in {% %} and can perform various functions like looping, conditionals, including other templates, etc.

### Common Template Tags:
- `{% for %}:` Iterates over a sequence.
- `{% if %}:` Conditional statement.
- `{% block %}:` Defines a block for template inheritance.
- `{% extends %}:` Indicates that a template inherits from a parent template.
- `{% include %}:` Includes another template.

Example:

```python
{% if user.is_authenticated %}
    <p>Welcome, {{ user.username }}!</p>
{% else %}
    <p>Please log in.</p>
{% endif %}
```

## 3. Filters
Filters modify the value of a variable before it is displayed. They are added to the variable with a pipe | character.

Example:

```python
<p>Today is {{ today|date:"F j, Y" }}</p>
<p>{{ name|upper }}</p>
```

## 4. Template Inheritance
Template inheritance allows you to define a base template and extend it in child templates. This promotes reusability and consistency.

Base Template (base.html):

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>{% block title %}My Site{% endblock %}</title>
</head>
<body>
    <header>
        <h1>My Site</h1>
    </header>
    <nav>
        <ul>
            <li><a href="/">Home</a></li>
            <li><a href="/about/">About</a></li>
        </ul>
    </nav>
    {% block content %}{% endblock %}
</body>
</html>
```

Child Template (home.html):

```python
{% extends "base.html" %}

{% block title %}Home{% endblock %}

{% block content %}
    <h2>Welcome to the homepage!</h2>
    <p>This is the home page of my site.</p>
{% endblock %}
```

## 5. Template Comments
Comments are ignored during template rendering and are used to leave notes within the template files. They are enclosed in {# #}.

Example:

```html
{# This is a comment #}
```

## 6. Template Context
The context is a dictionary of variables passed from the view to the template. You access these variables in the template using their keys.

Example View:

```python
from django.shortcuts import render

def my_view(request):
    context = {
        'name': 'John',
        'age': 30,
        'items': ['Apple', 'Banana', 'Orange']
    }
    return render(request, 'myapp/index.html', context)
```

Example Template (index.html):

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>My Template</title>
</head>
<body>
    <h1>Hello, {{ name }}!</h1>
    <p>You are {{ age }} years old.</p>
    <ul>
        {% for item in items %}
            <li>{{ item }}</li>
        {% endfor %}
    </ul>
</body>
</html>
```

## 7. Custom Template Tags and Filters
You can create custom template tags and filters to extend the functionality of the Django template engine.

### Example of a Custom Filter:
1. Create a templatetags directory in your app and add an __init__.py file to it.
2. Create a new Python file for your custom filters, e.g., custom_filters.py.

```python
# myapp/templatetags/custom_filters.py
from django import template

register = template.Library()

@register.filter
def multiply(value, arg):
    return value * arg
```

3. Load and use the custom filter in your template.

```python
{% load custom_filters %}
<p>{{ 4|multiply:2 }}</p>  <!-- Output: 8 -->
```

## 8. Escaping
Django automatically escapes variables to prevent cross-site scripting (XSS) attacks. If you need to mark a variable as safe HTML, you can use the safe filter.

Example:

```python
<p>{{ some_html|safe }}</p>
```

## 9. Including Other Templates
The {% include %} tag allows you to include the contents of another template inside the current template.

Example:

```python
{% include "myapp/header.html" %}
```

### Conclusion
The Django Template Language provides a robust and flexible system for rendering dynamic HTML content. By using variables, tags, filters, inheritance, and custom extensions, you can create complex and dynamic web pages efficiently and maintainably. Understanding how to use the Django Template Language is crucial for building effective and interactive web applications with Django.



