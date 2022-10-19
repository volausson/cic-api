from rest_framework import serializers
from .models import Comment


class CommentSerializer():
    owner = seralizers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.img.url')

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    class Meta:
        model = Comment
        fields = [
            'id', 'is_owner', 'profile_id', 'profile_image', 'post',
            'created_at', 'updated_at', 'content'
        ]