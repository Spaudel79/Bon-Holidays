from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.views.generic import DetailView, ListView, UpdateView

from .models import UserProfile

@login_required
def profile_redirector(request):
    return redirect('accounts:userprofile', username=request.user.email)