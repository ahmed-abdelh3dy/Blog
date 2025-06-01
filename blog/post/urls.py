from django.urls import path
from .views import PostView , PostDetailView , StatusView



urlpatterns = [
    path('create' , PostView.as_view()),
    path('status' , StatusView.as_view()),
    path('action/<int:id>' , PostDetailView.as_view())
]
