# Django Templates

Django templates are HTML files with special syntax that allows for dynamic content rendering. They enable you to generate HTML dynamically by injecting Python variables, loops, conditionals, and other control structures directly into the HTML markup. Here’s a comprehensive guide to Django templates:

## 1. Template Loading
Django templates are typically stored in the templates directory within each Django app. Django uses a template loader to load templates from this directory.

Example Directory Structure:

```bash
myapp/
├── templates/
│   └── myapp/
│       └── index.html
```

# 2. Rendering Templates
To render a template, you use Django's render() function in your views. This function takes the request object, template name, and a context dictionary containing data to be rendered in the template.

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

## 3. Template Variables
You can access variables passed from the view in the template using double curly braces {{ variable }}.

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

## 4. Template Tags
Django templates support template tags, which allow for logic and control flow within the template.

### Example Template Tags:
- `{% for %}:` Iterates over a list or queryset.
- `{% if %}:` Conditionally displays content.
- `{% block %} and {% extends %}:` Used for template inheritance.
- `{% include %}:` Includes another template.

## 5. Filters
Filters modify the output of template variables or tag parameters. They are applied by using the pipe character | after the variable or tag parameter.

### Example Filters:
- `{{ variable|upper }}:` Converts text to uppercase.
- `{{ variable|lower }}:` Converts text to lowercase.
- `{{ variable|date:"Y-m-d" }}:` Formats a date.

## 6. Template Inheritance
Django templates support inheritance, allowing you to create a base template with common elements and extend it in child templates.

Example Base Template (base.html):

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>{% block title %}My Site{% endblock %}</title>
</head>
<body>
    {% block content %}
    {% endblock %}
</body>
</html>
```

Example Child Template (child.html):

```python
{% extends "myapp/base.html" %}

{% block title %}My Page{% endblock %}

{% block content %}
    <h1>Hello, {{ name }}!</h1>
{% endblock %}
```

## 7. Comments
You can add comments to Django templates using the {# comment #} syntax. Comments are ignored during template rendering.

Example Comment:

```python
{# This is a comment #}
```

## 8. Escaping Output
By default, Django auto-escapes template variables to prevent cross-site scripting (XSS) attacks. You can use the safe filter to disable escaping for trusted content.

Example:

```python
{{ content|safe }}
```

## 9. Debugging Templates
Django provides template debugging tools to help troubleshoot template issues. You can enable template debugging in your Django settings.

```python
# settings.py
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'OPTIONS': {
            'debug': True,
            # Other options...
        },
    },
]
```

### Conclusion
Django templates provide a powerful and flexible way to generate HTML dynamically. By combining template variables, tags, filters, and template inheritance, you can create complex and dynamic web pages with ease. Understanding Django templates is essential for building dynamic web applications with Django.