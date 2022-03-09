from .tasks import send_mails, say
from apps.blogs.models import BlogPost, Subscribers
from django.db.models.signals import post_save
from django.dispatch import receiver


def email_task(sender, instance, created, **kwargs):
    if created:
        print("@signals.py")
        say()
        send_mails.delay()
        # send_mails.apply_async((kwargs={'param1':5, 'param2':0}, countdown=60)
        # send_mails.apply_async(args=(5,))


post_save.connect(email_task, sender=BlogPost, dispatch_uid="email_task")
