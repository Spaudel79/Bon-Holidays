from .tasks import send_mails
from apps.blogs.models import BlogPost,Subscribers
from django.db.models.signals import post_save
from django.dispatch import receiver


@receiver(post_save, sender=BlogPost)
def email_task(sender, instance, created, **kwargs):
    print(123456789)
    if created:
        print(123456789)
        subscribers = Subscribers.objects.all()
        blog = BlogPost.objects.latest('date_created')
        print(blog)
        # task = send_mails(subscribers, blog)
        # task.delay()
        # send_mails.delay(subscribers,blog)
        send_mails.apply_async(subscribers,blog)

# post_save.connect(email_task, sender=BlogPost)