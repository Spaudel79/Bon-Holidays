from __future__ import absolute_import, unicode_literals
from celery import shared_task

# from celery.decorators import task
from apps.blogs.models import BlogPost, Subscribers
from django.core.mail import send_mail
from travel_crm.settings import EMAIL_HOST_USER
from time import sleep


@shared_task
def say():
    print("before mail")


# @task(name='send_mails')
@shared_task()
def send_mails():
    print("@send_mails.py")
    subscribers = Subscribers.objects.all()
    blog = BlogPost.objects.latest("date_created")
    for abc in subscribers:
        # sleep(duration)
        print("i am inside loop")
        emailad = abc.email
        send_mail(
            "New Blog Post ",
            f" Checkout our new blog with title {blog.title} ",
            EMAIL_HOST_USER,
            [emailad],
            fail_silently=False,
        )
