from rest_framework import serializers
from .models import Post, Comment, CommentLike, PostLike

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'user', 'title', 'body', 'created']