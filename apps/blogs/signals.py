from apps.blogs.celery_files.tasks import send_mails
from apps.blogs.models import BlogPost,Subscribers
from django.db.models.signals import post_save
from django.dispatch import receiver






def email_task(sender, instance, created, **kwargs):
    print(123456789)
    if created:
        print(123456789)
        send_mails.delay()


post_save.connect(email_task, sender=BlogPost,dispatch_uid="email_task")