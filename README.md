# Travel CRM Backend

Backend for Travel CRM

Setup: <br>
Environment Setup
* `virtualenv -p </location/to/python3.7> venv` <br>
* `pip install -r requirements.txt`
w
Database Migrations
* `python manage.py makemigrations`
* `python manage.py migrate`

Creating SuperUser (customized to use Email and Password default in Django being username and password)
* `python manage.py createsuperuser`

Runserver
* `python manage.py runserver`

Admin Dashboard
* `http://127.0.0.1:8000/admin/`


*** Deployment Configuration

/etc/systemd/system/gunicorn.service

[Unit]
Description=gunicorn daemon
After=network.target

[Service]
User=aakashlabs
Group=www-data
WorkingDirectory=/home/aakashlabs/rupseonline
ExecStart=/home/aakashlabs/rupseonline/venv/bin/gunicorn --access-logfile - --workers 3 --bind unix:/run/gunicorn.sock travel_crm.wsgi:application

[Install]
WantedBy=multi-user.target


**
sudo systemctl start gunicorn
sudo systemctl enable gunicorn
systemctl daemon-reload


#for eb ssh
eb ssh
cd /var/app/current/
sudo nano travel_crm/settings.py
