from __future__ import absolute_import, unicode_literals
from travel_crm.celery import app as celery_app

__all__ = ("celery_app",)

print("celery is loaded")

# default_app_config = 'blogs.apps.BlogsConfig'
