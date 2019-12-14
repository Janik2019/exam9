from webapp.models import Like, Comment
from rest_framework import serializers


class CommentSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(read_only=True)

    class Meta:
        model = Comment
        fields = ('id', 'descr', 'created_at', 'author','photo')


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ('id', 'photo', 'user')




# ./manage.py dumpdata --indent=2 webapp auth.user > webapp/fixtures/dump.json