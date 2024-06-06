# Introduction to Databases & Models in Django
Django’s database layer, known as the Object-Relational Mapping (ORM) system, provides an abstraction over raw SQL to allow developers to interact with the database using Python code. This allows for database manipulation and querying in a more intuitive and Pythonic way. Here’s an overview of how databases and models work in Django:

## 1. What is a Database?
A database is a structured collection of data that can be accessed and manipulated. In web development, databases are used to store information such as user accounts, blog posts, product information, etc. Common types of databases include:

- `Relational Databases:` These use tables to store data and are queried using SQL (Structured Query Language). Examples include PostgreSQL, MySQL, SQLite, and Oracle.

- `NoSQL Databases:` These are non-tabular and store data differently. Examples include MongoDB, Cassandra, and Redis.

## 2. Django ORM (Object-Relational Mapping)
Django ORM is a powerful feature that allows you to interact with the database using Python classes and methods instead of writing raw SQL queries. Each model class represents a table in the database, and each instance of the class represents a row in the table.

## 3. Defining Models
A Django model is a Python class that subclasses django.db.models.Model. Each attribute of the model represents a database field.

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

## 4. Field Types
Django provides various field types to represent different kinds of data. Some common field types include:

- `CharField:` For short text fields.
- `TextField:` For long text fields.
- `IntegerField:` For integer values.
- `FloatField:` For floating-point numbers.
- `DateField:` For date values.
- `DateTimeField:` For date and time values.
- `BooleanField:` For true/false values.
- `EmailField:` For email addresses.
- `ForeignKey:` For creating many-to-one relationships.

## 5. Applying Migrations
After defining your models, you need to create and apply migrations. Migrations are a way of propagating changes you make to your models (adding a field, deleting a model, etc.) into the database schema.

### Creating Migrations:
```bash
python manage.py makemigrations
```

### Applying Migrations:
```bash
python manage.py migrate
```

## 6. Basic CRUD Operations
Once your models and migrations are set up, you can perform basic CRUD (Create, Read, Update, Delete) operations using Django’s ORM.

Creating an Object:
```python
# In the Django shell or a view
from myapp.models import Author

author = Author(name="John Doe", email="john.doe@example.com")
author.save()
```

Reading Objects:
```python
# Get all authors
authors = Author.objects.all()

# Get a single author by ID
author = Author.objects.get(id=1)

# Filter authors by a field
authors = Author.objects.filter(name="John Doe")
```

Updating an Object:
```python
author = Author.objects.get(id=1)
author.email = "new.email@example.com"
author.save()
```

Deleting an Object:
```python
author = Author.objects.get(id=1)
author.delete()
```

## 7. QuerySet API
Django’s ORM uses QuerySets to retrieve data from the database. QuerySets can be filtered, ordered, and manipulated to retrieve the exact data you need.

Example of QuerySet Methods:
```python
# Get all books published after a certain date
from datetime import date
books = Book.objects.filter(publication_date__gt=date(2020, 1, 1))

# Order books by title
books = Book.objects.order_by('title')

# Chain multiple QuerySet methods
books = Book.objects.filter(author__name="John Doe").order_by('-publication_date')
```

## 8. Model Relationships
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

### Conclusion
Django’s database and model system provide a robust and efficient way to interact with databases through Python code. By defining models, creating migrations, and using Django’s ORM, you can easily manage and manipulate your application’s data without writing complex SQL queries. Understanding these concepts is essential for building dynamic, data-driven web applications with Django.