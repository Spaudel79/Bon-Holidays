from rest_framework import viewsets, mixins
from .models import  BlogPost, Comment
from .serializers import BlogPostSerializer, CommentSerializer

class BlogPostViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer

class CommentViewSet(mixins.CreateModelMixin, mixins.RetrieveModelMixin,viewsets.GenericViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer