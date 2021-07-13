import os
from celery import Celery
from django.conf import settings
from __future__ import absolute_import

os.environ.setdefault('DJANGO_SETTINGS_MODULE','travel_crm.settings')

app = Celery('travel_crm')
app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))