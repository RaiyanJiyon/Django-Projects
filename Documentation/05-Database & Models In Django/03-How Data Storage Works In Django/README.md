# How Data Storage Works In Django

In Django, data storage is managed through the ORM (Object-Relational Mapping) system, which allows you to interact with the database using Python objects instead of writing raw SQL queries. Here’s a detailed explanation of how data storage works in Django:

## 1. Setting Up the Database
Django supports several databases out of the box, including PostgreSQL, MySQL, SQLite, and Oracle. You configure the database settings in the settings.py file of your Django project.

Example Configuration for SQLite (default):
```python
# settings.py
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / "db.sqlite3",
    }
}
```

Example Configuration for PostgreSQL:
```python
# settings.py
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'mydatabase',
        'USER': 'mydatabaseuser',
        'PASSWORD': 'mypassword',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

## 2. Defining Models
Models in Django are Python classes that subclass django.db.models.Model. Each attribute of the class represents a database field.

Example:
```python
# models.py
from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()

class Book(models.Model):
    title = models.CharField(max_length=200)
    publication_date = models.DateField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
```

## 3. Creating and Applying Migrations
Migrations are Django’s way of propagating changes you make to your models into the database schema. They ensure your database schema is in sync with your current set of models.

Creating Migrations:
```bash
python manage.py makemigrations
```

Applying Migrations:
```bash
python manage.py migrate
```

## 4. Working with the Database Using Django ORM
Once the models are defined and migrations are applied, you can perform CRUD (Create, Read, Update, Delete) operations using Django’s ORM.

Creating Records:
```python
# In Django shell or views
from myapp.models import Author

# Create and save a new author
author = Author(name="John Doe", email="john.doe@example.com")
author.save()
```

Reading Records:
```python
# Get all authors
authors = Author.objects.all()

# Get a single author by ID
author = Author.objects.get(id=1)

# Filter authors by a field
authors = Author.objects.filter(name="John Doe")
```

Updating Records:
```python
author = Author.objects.get(id=1)
author.email = "new.email@example.com"
author.save()
```

Deleting Records:
```python
author = Author.objects.get(id=1)
author.delete()
```

## 5. QuerySets and QuerySet API
A QuerySet is a collection of database queries that Django executes against the database. QuerySets allow you to filter, order, and manipulate data in the database.

Example of QuerySet Operations:
```python
# Get all books published after a certain date
from datetime import date
books = Book.objects.filter(publication_date__gt=date(2020, 1, 1))

# Order books by title
books = Book.objects.order_by('title')

# Chain multiple QuerySet methods
books = Book.objects.filter(author__name="John Doe").order_by('-publication_date')
```

## 6. Model Relationships
Django models can define relationships between each other using fields such as ForeignKey, OneToOneField, and ManyToManyField.

Example:
```python
class Publisher(models.Model):
    name = models.CharField(max_length=200)

class Book(models.Model):
    title = models.CharField(max_length=200)
    publication_date = models.DateField()
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    authors = models.ManyToManyField(Author)
```

## 7. Using the Admin Interface
Django includes a powerful admin interface that can be used to manage your application’s data.

Enabling the Admin Interface:
```python
# In your app's admin.py
from django.contrib import admin
from .models import Author, Book

admin.site.register(Author)
admin.site.register(Book)
```

## 8. Data Validation and Constraints
Django models come with built-in data validation and constraints that help ensure the integrity of the data.

Example:
```python
class Author(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)  # Ensures unique email addresses
```

## 9. Advanced Data Storage Features
- `Custom Managers and QuerySets:` Define custom database query logic.
- `Signals:` Hook into the life cycle of models to execute code when certain actions occur.
- `Aggregation and Annotation:` Perform complex database queries and calculations.

Example of Custom Manager:
```python
class BookManager(models.Manager):
    def published(self):
        return self.filter(publication_date__isnull=False)

class Book(models.Model):
    title = models.CharField(max_length=200)
    publication_date = models.DateField(null=True, blank=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    objects = BookManager()
```

### Conclusion
Data storage in Django revolves around the ORM, which abstracts database interactions into Python objects and methods. This approach simplifies database operations, ensures data integrity, and allows for complex queries and relationships, making Django a powerful tool for web development.

