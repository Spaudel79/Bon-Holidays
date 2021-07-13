from django.urls import path
from . import views

urlpatterns = [
    # path('', views.Homepage.as_view(), name='home'),
    path('api/register', views.RegisterUserView.as_view(), name='api-register'),
    path('api/login', views.LoginUserView.as_view(), name='api-login'),
    path('api/logout', views.Logout.as_view(), name='api-logout'),
    path('api/users', views.UsersListView.as_view(), name='api-users'),
    path('api/profile', views.ProfileListView.as_view(), name='api-profile'),
    # path('blog-post/<int:pk>', views.BlogPostDetailsListAPIView.as_view(), name='api-blog-post_details'),
    # path('comments/', views.CommentCreateAPIView.as_view(), name='api-comments'),
    path('api/subscriber',views.SubscribersView.as_view(),name='api-subsciber')

]
