from rest_framework import serializers
from . models import Post



class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'
        read_only_fields = ('user',)



    def create(self, validated_data):
        user = self.context['user']
        return Post.objects.create(user_id=user, **validated_data)
