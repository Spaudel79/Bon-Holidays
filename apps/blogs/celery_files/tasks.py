from __future__ import absolute_import, unicode_literals
from celery import shared_task
# from celery.decorators import task
from apps.blogs.models import BlogPost,Subscribers

from django.db.models.signals import post_save
from django.core.mail import send_mail

from travel_crm.settings import EMAIL_HOST_USER

@shared_task
def send_mails(self,*args, **kwargs):

    subscribers = self.kwargs['subscribers']
    blog = self.kwargs['blog']
    for abc in subscribers:
        emailad = abc.email
        send_mail('New Blog Post ', f" Checkout our new blog with title {blog.title} ",
                  EMAIL_HOST_USER, [emailad],
                  fail_silently=False)

    # if created:
    #     blog = BlogPost.objects.latest('date_created')
    #     for abc in subscribers:
    #         emailad = abc.email
    #         send_mail('New Blog Post ', f" Checkout our new blog with title {blog.title} ",
    #                   EMAIL_HOST_USER, [emailad],
    #                   fail_silently=False)
    # else:
    #     return






