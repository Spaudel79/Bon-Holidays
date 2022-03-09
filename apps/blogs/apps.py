from django.apps import AppConfig


class BlogsConfig(AppConfig):
    name = "apps.blogs"

    def ready(self):
        print("working")
        from apps.blogs import signals  # noqa

        print("after import")
