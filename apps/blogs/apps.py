from django.apps import AppConfig


class BlogsConfig(AppConfig):
    name = "apps.blogs"

    # def ready(self):
    #     print("inside ready")
    #     import apps.blogs.celery_files.signals #noqa
