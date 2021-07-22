from __future__ import absolute_import, unicode_literals
# from celery.task import task
# from celery import shared_task
from celery.decorators import task
# from apps.blogs.models import BlogPost,Subscribers
import time
from django.db.models.signals import post_save
from django.core.mail import send_mail
from travel_crm.celery import app
from travel_crm.settings import EMAIL_HOST_USER

# @task(name='say')


# @shared_task
@task(name='say')
def say(duration):
    time.sleep(duration)
    return print("iam inside 1st task")

# @shared_task
# def send_mails():
#     print("I am here")
#     # subscribers = kwargs['subscribers']
#     # blog = kwargs
#     subscribers = Subscribers.objects.all()
#     blog = BlogPost.objects.latest('date_created')
#     for abc in subscribers:
#         emailad = abc.email
#         send_mail('New Blog Post ', f" Checkout our new blog with title {blog.title} ",
#                   EMAIL_HOST_USER, [emailad],
#                   fail_silently=False)


# @shared_task
# def sum():
#     time.sleep(5)
#     print("sum is working")



