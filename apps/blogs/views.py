from rest_framework import viewsets, mixins
from .models import *
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from django.shortcuts import get_object_or_404
from .pagination import *
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from django.core.mail import send_mail
from travel_crm.settings import EMAIL_HOST_USER
from rest_framework import status

from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
)

from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
)


class BlogPostListFrontAPIView(ListAPIView):
    permission_classes = [AllowAny]
    queryset = BlogPost.objects.all().order_by("-date_created")[:3]
    serializer_class = BlogPostFrontPageSerializer


class BlogPostAllListAPIView(ListAPIView):
    permission_classes = [AllowAny]
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostAllSerializer
    pagination_class = BlogPostPageNumberPagination

    def get_queryset(self):
        tag = self.request.query_params.get("tag", None)
        if tag is not None:
            return BlogPost.objects.select_related("destination").filter(
                tag__tagname=tag
            )
        else:
            return BlogPost.objects.select_related("destination")


class BlogPostDetailsListAPIView(ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = BlogPostDetailSerializer

    # pagination_class = CommentPageNumberPagination
    def get_queryset(self):
        return BlogPost.objects.select_related("destination").filter(
            pk=self.kwargs["pk"]
        )


class CommentCreateAPIView(CreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Comment.objects.all()
    serializer_class = CommentListSerializer

    def perform_create(self, serializer):

        blog = get_object_or_404(BlogPost, pk=self.kwargs["pk"])
        serializer.save(user=self.request.user, blog=blog)

        name = serializer.data["name"]
        email = serializer.data["email"]
        subject = serializer.data["subject"]

        send_mail(
            "New Comment ",
            f"Comment has been made by {name} "
            f"having email {email} "
            f"and subject as '{subject}'",
            email,
            ["sales6@bonholidays.com.np"],
            fail_silently=False,
        )

    # def get_context_data(self, **kwargs):
    #     context = super(CommentCreateAPIView, self).get_context_data(**kwargs)
    #     pk = self.kwargs['pk']
    #     context['post'] = BlogPost.objects.filter(id=pk)
    #     return context


class CommentListAPIView(ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = CommentListSerializer

    def get_queryset(self):
        return Comment.objects.select_related("user", "blog").filter(
            blog=self.kwargs["blog"]
        )


class TagsAPIView(ListAPIView):
    permission_classes = [AllowAny]
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


from apps.blogs.admin import BlogForm


def blogform(request):
    if request.method == "POST":
        form = BlogForm(request.POST)
        if form.is_valid():
            form.save()


class SubscribersView(APIView):
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = SubscriberSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message": "You have been subscribed"}, status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors)
