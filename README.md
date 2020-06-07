# Aakash-Backend

Backend for Aakash CRM

Setup: <br>
Environment Setup
* `virtualenv -p </location/to/python3.7> venv` <br>
* `pip install -r requirements.txt`

Database Migrations
* `python manage.py makemigrations`
* `python manage.py migrate`

Creating SuperUser (customized to use Email and Password default in Django being username and password)
* `python manage.py createsuperuser`

Runserver
* `python manage.py runserver`

Admin Dashboard
* `http://127.0.0.1:8000/admin/`
