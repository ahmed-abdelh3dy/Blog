from django.urls import path
from .views import CommetView , CommentViewDetail


urlpatterns = [
    path('comment' , CommetView.as_view()),
    path('comment/<int:id>' , CommentViewDetail.as_view())
]
