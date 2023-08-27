it is a django based projectt.
first to initialliaze need to install python and its libraries and then install django using pip install django .
after installing django need to open terminal and make project with command django-admin startproject Assignmnet.
after making project need to create app using command django-admin startapp AssignmnetApp 
Now go to settings.py under Project folder in INSTALLED APPS give the ap name AssignmnetApp.
Coming to databse
Need to install mysql in pc ( i installed mysql workbench)
After setting up mysql need to create database with the name user using command CREATE DATABASE users;
Then on left side of the window new database would appear click on that and make table inisde that
For creating table with name user need to write command 
CREATE TABLE users (
    id INT PRIMARY KEY,
    name VARCHAR(200),
    email VARCHAR(100),
    role VARCHAR(50)
);
Now a table is created.
Coming back to django in the terminal connect mysql to djnago using pip install mysqlclient
mysql would be installed in django.
Go to setting.py again and in databases instead of sqlite we are using 
'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'name of database',
        'USER': 'name of user',
        'PASSWORD': 'enter you password ',
        'HOST': 'host server', 
        'PORT': '3306',       # Default MySQL port
    }
Now in django terminal run command python manage.py makemigrations.
After that run python manage.py migrate.
Django project connected to mysql with all tables.

Now need to create all functions in views.py for retrieving all users, adding new user to database, getting hello world page.
Need to create a template folder where all templates files would be there.
Need to create template for each page acording to requirement.
In the urls.py mention the path with name of its respective view.

Now when all of this done in the terminal run " python manage.py runserver" which will run the project on web browser.

 
