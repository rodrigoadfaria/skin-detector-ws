from rest_framework import serializers

from authentication.serializers import AccountSerializer
from posts.models import Post


class PostSerializer(serializers.ModelSerializer):
    """
    read_only=True because we should not be updating an Account object with a
    PostSerializer. We also set required=False here because we will set the
    author of this post automatically.
    """
    author = AccountSerializer(read_only=True, required=False)

    class Meta:
        model = Post

        fields = ('id', 'author', 'content', 'created_at', 'updated_at')
        read_only_fields = ('id', 'created_at', 'updated_at')

    def get_validation_exclusions(self, *args, **kwargs):
        exclusions = super(PostSerializer, self).get_validation_exclusions()

        return exclusions + ['author']