from django.db import models
from mini_insta.models import Post
from rest_framework import serializers

# Create your models here.
class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('author','title','posted_on')
