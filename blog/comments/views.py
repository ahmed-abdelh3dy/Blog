from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import CommentSerializer
from .models import Comments
from post.models import Post
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication


class CommetView(APIView):
    # permission_classes = [IsAuthenticated]
    # authentication_classes = [JWTAuthentication]

    def post(self, request):
        user = request.user.id
        post_id = request.data.get('post')
        post = get_object_or_404(Post, id=post_id)
        comment = CommentSerializer(data=request.data, context={'user': user, 'post': post})
        if comment.is_valid():
            comment.save()
            return Response({'message': 'comment is created', 'comment': comment.data}, status=status.HTTP_201_CREATED)
        return Response({'error': comment.errors}, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        comments = Comments.objects.all()
        serializer = CommentSerializer(comments, many=True)
        return Response({'list of comments': serializer.data}, status=status.HTTP_200_OK)

class CommentViewDetail(APIView):

    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]


    def put(self  , request , id):
        comment = get_object_or_404 (Comments , id = id)
        serializer = CommentSerializer(comment , data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({' post data' :serializer.data} , status=status.HTTP_200_OK)


    def get(self  , request , id):
        comment = get_object_or_404 (Comments , id = id)
        serializer = CommentSerializer(comment)
        return Response({' post data' :serializer.data} , status=status.HTTP_200_OK)

    def delete(self  , request , id):
        comment = get_object_or_404 (Comments , id = id)
        comment.delete()
        return Response({'comment deleted'})