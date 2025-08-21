# posts/views.py
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Post, Like
from notifications.models import Notification

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def like_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    
    # Check if the user has already liked the post
    like, created = Like.objects.get_or_create(user=request.user, post=post)
    
    if not created:
        return Response({'detail': 'You have already liked this post.'}, status=status.HTTP_409_CONFLICT)
    
    # Create a notification for the post's owner
    if request.user != post.author:
        Notification.objects.create(
            recipient=post.author,
            actor=request.user,
            verb='liked your post',
            target=post
        )
    
    return Response({'detail': 'Post liked successfully.'}, status=status.HTTP_201_CREATED)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def unlike_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    
    try:
        like = Like.objects.get(user=request.user, post=post)
        like.delete()
        return Response({'detail': 'Post unliked successfully.'}, status=status.HTTP_204_NO_CONTENT)
    except Like.DoesNotExist:
        return Response({'detail': 'You have not liked this post.'}, status=status.HTTP_404_NOT_FOUND)