from rest_framework.serializers import ModelSerializer
from webapp.models import Photo, Comment
from rest_framework import serializers



class CommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'descr', 'photo', 'author', 'created_at']


class PhotoSerializer(serializers.ModelSerializer):
    # comment_foto = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Photo
        fields = ('id', 'photo', 'signature', 'created_at',
                  'rating', 'author')