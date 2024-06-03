# Installing Django on Windows

To install Django on a Windows machine, follow these steps:

## Step 1: Prerequisites

Before installing Django, make sure you have Python installed on your system. You can follow the instructions for installing Python on Windows provided earlier.

## Step 2: Install Django using pip

1. Open Command Prompt by typing `cmd` in the search bar and hitting Enter.
2. In Command Prompt, type the following command and press Enter to install Django using pip:

```bash
pip install django
```

This command will download and install the latest version of Django and its dependencies.

## Step 3: Verify the Installation
After the installation is complete, you can verify that Django is installed correctly by typing the following command in Command Prompt:

```bash
django-admin --version
```

You should see the installed version of Django printed on the screen.

## Step 4: Create a Django Project (Optional)
You can create a new Django project to test the installation. Navigate to the directory where you want to create the project using Command Prompt and run the following command:

```bash
django-admin startproject myproject
```

Replace `myproject` with the name of your project.

## Step 5: Run the Development Server
Navigate into the newly created project directory:

```bash
cd myproject
```

Then, start the development server by running the following command:

```bash
python manage.py runserver
```

This will start the development server, and you can access your Django project by visiting http://127.0.0.1:8000 in your web browser.

### Conclusion
You have successfully installed Django on your Windows machine. You can now start building web applications using Django framework.