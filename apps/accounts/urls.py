# packages/urls.py
from django.urls import include, path
from django.conf.urls import url
from . import views

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^accounts/userprofile/$', views.profile_redirector, name='user_profile'),
]

app_name = 'accounts'