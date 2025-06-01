from django.urls import path
from .views import PostView , PostDetailView , StatusView



urlpatterns = [
    path('post' , PostView.as_view()),
    path('post/status' , StatusView.as_view()),
    path('post/<int:id>' , PostDetailView.as_view())
]
