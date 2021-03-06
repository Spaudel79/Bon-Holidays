"""travel_crm URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
import debug_toolbar
from rest_framework.authtoken.models import Token

urlpatterns = [
    path("", include("apps.accounts.urls")),
    path("", include("apps.blogs.urls")),
    path("", include("apps.enquiry.urls")),
    path("", include("apps.packages.urls")),
    path("", include("apps.booking.urls")),
    path("", include("apps.logo.urls")),
    path("", include("apps.office.urls")),
    path("", admin.site.urls),
    path("admin/", admin.site.urls),
    path("ckeditor", include("ckeditor_uploader.urls")),
    # path("__debug__/", include(debug_toolbar.urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# ]+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


# if settings.DEBUG is True:
#     urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [
        url(r"^__debug__/", include(debug_toolbar.urls)),
    ] + urlpatterns

admin.site.unregister(Token)
