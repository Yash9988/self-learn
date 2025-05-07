# Django Terminologies

## Structure
    - Models: Handles database interactions
    - Views: Handles business logic and return responses
    - Templates: Handles HTML content with dynamic data

Request & Response Objects: Used to manage data between client and server.



# Log of Steps


## Start a new Django project

1. Create a new Django project
    - Run `django-admin startproject firstproject`
        - Creates a new Django project with the name `firstproject`

2. Navigate inside the firstproject directory and create a new Django app called `firstapp`.
    - Run `python manage.py startapp firstapp`
        - This command creates a new directory called `firstapp` with all necessary files for a Django application

## Views & URL Patterns

3. Define views in `firstapp/views.py` to handle requests and return responses.
    - Create a dummy view function that returns "Hello World!" when accessed.
    - Create another view class that handles GET requests and returns "Hello India!" when accessed.

4. Create a new file called `urls.py` inside the `firstapp` directory to define URL patterns for your views.
    - Import the views from `views.py`
    - Define URL patterns using Django's path function.

5. Navigate inside the `firstproject` directory and open the `urls.py` file located at `firstproject/urls.py`.
    - Import the include function from django.urls module.
    - Add a new URL pattern, `app/`, that includes the URLs defined in `firstapp/urls.py`

6. Append `firstapp` to the `INSTALLED_APPS` list in `firstproject/settings.py`.

7. Run the Django development server by running `python manage.py runserver`
    - Access your application by visiting http://127.0.0.1:8000/app/function and http://127.0.0.1:8000/app/class in your web browser.
        - You should see "Hello World!" and "Hello India!" respectively.


## Models & Forms

8. Next, navigate to the file called `models.py` inside the `firstapp` directory to define database models for your application.
    - Define a new model class called `MenuItem`, which inherits from models.Model, that represents a menu item with fields for name (CharField) and price (IntegerField).
    - Define another model class called `Reservation`, that represents a reservation with fields for firstName, lastName, guestCount, reservationTime, and comments.
    - Run migrations by running `python manage.py makemigrations firstapp` and `python manage.py migrate`

9. Create a new file called `forms.py` inside the `firstapp` directory to define forms for your application.
    - Define a form class called `ReservationForm`, which inherits from forms.ModelForm, and add a nested `Meta` class that specifies the model and fields to include in the form.

10. In order to use the admin panel, we create a superuser by running `python manage.py createsuperuser` and following the prompts to enter a username, email address, and password.

11. To fill the form from the admin panel, we need to register the models with the admin site.
    - Open the file called `admin.py` inside the `firstapp` directory.
    - Register the form by appending `admin.site.register(Reservation)` to the file.
    - Run migrations by running `python manage.py makemigrations firstapp` and `python manage.py migrate`


## Switching from SQLite to MySQL Database

12. Create a new database in MySQL called `django_db` using the command: `CREATE DATABASE django_db;`

13. Install the MySQL adapter for Python by running `pip install mysqlclient`.

14. Now navigate to the Django project directory and open the file `settings.py`.
    - Update the `DATABASES` dictionary to use the MySQL database, along with the appropriate credentials and options.
    - Run migrations.
    - Login to mysql using the command: `mysql -u root -p` and enter the password when prompted.
    - Access the database by running the command: `USE django_db;`
    - Execute `show tables;` to verify that the tables have been created successfully and MySQL has been configured correctly.


## Templates

15. Create a new directory called `templates` inside the `firstapp` directory.
    - Inside this directory, create an HTML file named `index.html`.
        - Use `!` to generate the HTML template for the index page.

16. Updating the `index.html` file:
    - Rename the title tag in the `index.html` file to "Reservations".
    - Add a form element with the method attribute set to "POST" inside the body.
    - Since we are using Django forms, use `{{ form.as_p }}` to render the form fields as paragraphs within the form.
    - We also need to append a CSRF token to our form for security reasons. Use `{% csrf_token %}` before rendering the form fields.
    - Add a submit button with the type attribute set to "submit" and the text "Save".

17. Navigate back to the `views.py` file in the `firstapp` directory, to define the form variable that will be used in our template.
    - Create a new method called `home` which accepts `request` as its parameter.
    - Inside this method, instantiate a `ReservationForm()` object and assign it to a variable named `form`.
    - Check if the HTTP request method is "POST" using `if request.method == 'POST':`.
        - If yes, then update the form instance with the POST data by calling `form = ReservationForm(request.POST)`.
        - Return a success HttpResponse message
    - If no, render the `index.html` template and pass the `form` variable to it.
    - Finally, naviate to the `urls.py` file in the `firstapp` directory, to define the URL pattern for our new view.