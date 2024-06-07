# Passing Context To Templates

Passing context to templates in Django allows you to provide dynamic data to be rendered in the HTML. Context can include variables, lists, dictionaries, querysets, or any other Python objects needed to generate the content of the template. Here's how you can pass context to templates in Django:

## 1. Passing Context from Views
In your Django views, you can define a context dictionary containing the data you want to pass to the template. Then, you pass this context dictionary to the render() function along with the request object and the template name.

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

## 2. Accessing Context in Templates
In your template file (index.html in this case), you can access the data passed in the context using template variables enclosed in double curly braces ({{ }}).

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

## 3. Accessing QuerySet Data
If you're passing a QuerySet from the view to the template, you can iterate over it directly in the template using template tags.

Example QuerySet in View:

```python
from myapp.models import Post

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'myapp/post_list.html', {'posts': posts})
```

Example Template (post_list.html):

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Post List</title>
</head>
<body>
    <h1>Posts</h1>
    <ul>
        {% for post in posts %}
            <li>{{ post.title }}</li>
        {% endfor %}
    </ul>
</body>
</html>
```

## 4. Using Context Processors
Context processors are functions that run before the template is rendered and add data to the context for every template. Django provides several built-in context processors, such as django.template.context_processors.request, which adds the request object to the context.

Example Configuration in settings.py:

```python
# settings.py
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                # Other context processors...
            ],
        },
    },
]
```

## 5. Dynamic Context Data
You can generate context data dynamically in your view functions based on request parameters, database queries, or any other logic.

Example View:

```python
from django.shortcuts import render
from myapp.models import Product

def product_list(request, category_id):
    products = Product.objects.filter(category_id=category_id)
    context = {
        'category_id': category_id,
        'products': products
    }
    return render(request, 'myapp/product_list.html', context)
```

Example Template (product_list.html):

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Product List</title>
</head>
<body>
    <h1>Category {{ category_id }} Products</h1>
    <ul>
        {% for product in products %}
            <li>{{ product.name }}</li>
        {% endfor %}
    </ul>
</body>
</html>
```

### Conclusion
Passing context to templates in Django is essential for rendering dynamic content. By defining a context dictionary in your views and passing it to the render() function, you can provide data to be displayed in the HTML templates. Understanding how to pass context effectively is crucial for building dynamic and interactive web applications with Django.