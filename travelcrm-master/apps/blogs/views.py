from rest_framework import viewsets, mixins
from .models import *
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST

from rest_framework.generics import (
CreateAPIView, DestroyAPIView,
ListAPIView, UpdateAPIView,
RetrieveUpdateAPIView, RetrieveAPIView
)

from rest_framework.permissions import (
AllowAny, IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly
)


# class BlogPostViewSet(viewsets.ReadOnlyModelViewSet):
#     queryset = BlogPost.objects.all()
#     serializer_class = BlogPostSerializer
#
# class CommentViewSet(mixins.CreateModelMixin, mixins.RetrieveModelMixin,viewsets.GenericViewSet):
#     queryset = Comment.objects.all()
#     serializer_class = CommentSerializer

class BlogPostListAPIView(ListAPIView):
    queryset = BlogPost.objects.all().order_by('-date_created')[:3]
    # queryset = BlogPost.objects.all.order_by('-date_created')[:3]
    serializer_class = BlogPostSerializer

class BlogPostDetailsListAPIView(ListAPIView):
        # queryset = BlogPost.objects.filter(pk=pk)
        # queryset = BlogPost.objects.all.order_by('-date_created')[:3]
        serializer_class = BlogPostSerializer

        def get_queryset(self):
            return BlogPost.objects.filter(pk=self.kwargs['pk'])


class CommentCreateAPIView(CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


