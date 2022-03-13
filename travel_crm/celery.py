from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from django.conf import settings

# import django
#
# django.setup()  # This is key
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "travel_crm.settings")

app = Celery("travel_crm")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS, force=True)
# app.autodiscover_tasks()
print("iam inside project celery")


@app.task(bind=True)
def debug_task(self):
    print("Request: {0!r}".format(self.request))
