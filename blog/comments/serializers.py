from rest_framework import serializers
from .models import Comments



class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = '__all__'
        read_only_fields = ('user', 'post')

    def create(self, validated_data):
            user = self.context['user']
            post = self.context['post']
            return Comments.objects.create(user_id=user, post_id=post.id, **validated_data)
