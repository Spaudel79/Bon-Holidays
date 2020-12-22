from rest_framework import serializers
from .models import *
from .serializers import *

class CommentSerializer(serializers.ModelSerializer):
    # blog = serializers.StringRelatedField()
    class Meta:
        model = Comment
        fields = ['name', 'email', 'subject', 'comment']
        # depth = 1

class CommentListSerializer(serializers.ModelSerializer):
    # blog = serializers.StringRelatedField()
    class Meta:
        model = Comment
        fields = ['name', 'email', 'subject', 'comment']

class BlogPostFrontPageSerializer(serializers.ModelSerializer):
    # url = serializers.HyperlinkedIdentityField(view_name='api-blog-post', read_only=True)
    # tag = serializers.StringRelatedField()
    class Meta:
        model = BlogPost
        fields = ['id', 'image', 'title', 'caption', 'categories', 'tag', 'date_created']
        # fields = '__all__'
        depth = 1


class BlogPostAllSerializer(serializers.ModelSerializer):
    # tag = serializers.StringRelatedField()

    class Meta:
        model = BlogPost
        fields = ['id', 'image', 'title', 'caption', 'categories', 'tag', 'date_created', ]
        # fields = '__all__'
        depth = 1

        # def get_comments(self, obj):
        #     content_type = obj.get_content_type
        #     object_id = obj.id
        #     c_qs = Comment.objects.filter_by_instance()
        #     comments = CommentSerializer(c_qs, many=True).data
        #     return comments

        # def create(self, validated_data):
        #     comments = validated_data.pop('commnets')

class BlogPostDetailSerializer(serializers.ModelSerializer):
    # comments = serializers.SerializerMethodField()
    # comments = CommentSerializer(source='comments.content')
    # comments = CommentListSerializer(many=True)
    # url = serializers.HyperlinkedIdentityField(view_name='api-blog-post_details', read_only=True)
    comments = CommentSerializer(many=True)
    # tag = serializers.StringRelatedField()
    class Meta:
        model = BlogPost
        fields = ['id',  'image', 'title', 'categories', 'caption', 'content', 'tag', 'date_created', 'comments']
        # fields = '__all__'
        depth = 1


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'








class CommentListSerializer(serializers.ModelSerializer):
    # blog = serializers.StringRelatedField()
    class Meta:
        model = Comment
        fields = ['name', 'email', 'subject', 'comment']


class CommentPostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        # fields = '__all__'
        fields = ['name', 'email', 'subject', 'comment',]



 # fields = ('content', 'parent', 'author', 'reply_count', 'post')





class BlogListSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPost
        fields = '__all__'


class BlogPostCommentSerializer(serializers.ModelSerializer):
    # comments = serializers.SerializerMethodField()
    # comments = CommentSerializer(source='comments.content')
    # comments = CommentListSerializer(many=True)
    blog = BlogListSerializer(many=False)
    class Meta:
        model = Comment
        fields = ['blog', 'name', 'email', 'subject', 'comment',]
        # fields = '__all__'















