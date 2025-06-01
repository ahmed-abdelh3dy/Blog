from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
# imort token 
from rest_framework.authentication import TokenAuthentication

# import jwt 
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import status
from .permissions import isAbove18
from .serializers import PostSerializer
from .models import Post


class PostView(APIView):
    # use token auth 
    # authentication_classes = [TokenAuthentication]
    # use jwt 
    authentication_classes = [JWTAuthentication]

    permission_classes = [isAbove18  ,IsAuthenticated]

    def post(self, request):

        user = request.user.id
        print(f"User ID: {user}")
        post = PostSerializer(data=request.data, context={'user': user})
        if post.is_valid():
            post.save()
            return Response({'message': 'Post has been created', 'post': post.data}, status=status.HTTP_201_CREATED)
        return Response(post.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        if request.user.is_superuser:

            posts = Post.objects.all()
            serializer_posts = PostSerializer(posts, many=True)
            return Response({'posts_list': serializer_posts.data}, status=status.HTTP_200_OK)
        else:
            posts = Post.objects.filter(user= request.user)
            serializer_posts = PostSerializer(posts, many=True)
            return Response({'posts_list': serializer_posts.data}, status=status.HTTP_200_OK)


class PostDetailView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, id):
        post = get_object_or_404(Post, id=id)
        if post.user.id != request.user.id:
            return Response({'message': 'You  cant get this post'}, status=status.HTTP_403_FORBIDDEN)
        
        serializer_post = PostSerializer(post)
        return Response({'post': serializer_post.data}, status=status.HTTP_200_OK)

    def put(self, request, id):
        post = get_object_or_404(Post, id=id)
        if post.user.id != request.user.id:
            return Response({'message': 'You  cant edit this post'}, status=status.HTTP_403_FORBIDDEN)
        
        serializer_post = PostSerializer(post, data=request.data, context={'user': request.user.id})
        if serializer_post.is_valid():
            serializer_post.save()
            return Response({'message': 'Post has been updated', 'post': serializer_post.data}, status=status.HTTP_200_OK)
        return Response(serializer_post.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        post = get_object_or_404(Post, id=id)
        if post.user.id != request.user.id:
            return Response({'message': 'You  cant delete this post'}, status=status.HTTP_403_FORBIDDEN)
            
        post.delete()
        return Response({'message': 'Post has been deleted'}, status=status.HTTP_204_NO_CONTENT)
    

class StatusView(APIView):
    def get(self, request): 
        post_status  = request.data.get('status')
        posts = Post.objects.filter(status = post_status )
        serializer = PostSerializer(posts , many=True)
        return Response({ 'post status': serializer.data}, status=status.HTTP_200_OK)
          
