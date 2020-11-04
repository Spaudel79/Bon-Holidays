from rest_framework import viewsets, mixins
from .models import *
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from django.shortcuts import get_object_or_404
from .pagination import *


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

class BlogPostListFrontAPIView(ListAPIView):
    permission_classes = [AllowAny]
    queryset = BlogPost.objects.all().order_by('-date_created')[:3]
    # queryset = BlogPost.objects.all.order_by('-date_created')[:3]
    serializer_class = BlogPostFrontPageSerializer

class BlogPostAllListAPIView(ListAPIView):
    permission_classes = [AllowAny]
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostAllSerializer
    pagination_class = BlogPostPageNumberPagination

class BlogPostDetailsListAPIView(ListAPIView):
    permission_classes = [AllowAny]
    # queryset = BlogPost.objects.all()
    serializer_class = BlogPostDetailSerializer

    # pagination_class = CommentPageNumberPagination
    def get_queryset(self):
            return BlogPost.objects.filter(pk=self.kwargs['pk'])


class CommentCreateAPIView(CreateAPIView):
    permission_classes= [IsAuthenticated]
    queryset = Comment.objects.all()
    serializer_class = CommentListSerializer

    def perform_create(self, serializer):
        # user = self.request.user
        blog = get_object_or_404(BlogPost, pk= self.kwargs['pk'])
        serializer.save(blog=blog)
    # def get_queryset(self):
    #     return BlogPost.objects.filter(pk=self.kwargs['pk'])

    # def get(self, request, id=None):
    #     instance = self.get_object(id)
    #     serailizer = BlogListSerializer(instance)
    #     return Response(serailizer.data)

    #def.....
    # form.instance.blog_id = self.kwargs['pk']
    # return super().form_valid(form)

    # def get_object(self, id):
    #     try:
    #         return BlogPost.objects.get(id=id)
    #     except BlogPost.DoesNotExist as e:
    #         return Response({"error": "Given question object not found."}, status=404)

    # def post(self, request, format=None):
    #     name = request.data.get("name")
    #     email = request.data.get("email")
    #     subject = request.data.get("subject")
    #     comment = request.data.get("comment")
    #
    #     blog = request.data['blog']['id']
    #     data = {'name': name, 'email': email, 'subject': subject, 'comment': comment, 'blog': blog}
    #     serializer = BlogPostCommentSerializer(data=data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=serializers.status.HTTP_201_CREATED)
        # else:
        #     re



    # def get_context_data(self, **kwargs):
    #     context = super(CommentCreateAPIView, self).get_context_data(**kwargs)
    #     pk = self.kwargs['pk']
    #     context['post'] = BlogPost.objects.filter(id=pk)
    #     return context



    # def post(self, request):
    #     data = request.data
    #     serializer = CommentPostSerializer(data=data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=201)
    #     return Response(serializer.erros, status=400)


class CommentListAPIView(ListAPIView):
    permission_classes = [AllowAny]
    # queryset = Comment.objects.all()
    serializer_class = CommentListSerializer

    def get_queryset(self):
        return Comment.objects.filter(blog=self.kwargs['blog'])


