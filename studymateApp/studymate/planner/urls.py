from django.urls import path
from .views import CommentAPIView  # , ScheduleAPIView #, TodoAPIView
from .views import TodoCreateAPIView, TodoDetailAPIView, ScheduleCreateAPIView, ScheduleDetailAPIView, CommentCreateAPIView, CommentDetailAPIView

urlpatterns = [
    path('all/', CommentAPIView.as_view()),
    path('todo/post/', TodoCreateAPIView.as_view()),
    path('todo/<int:pk>/', TodoDetailAPIView.as_view()),
    path('schedule/post/', ScheduleCreateAPIView.as_view()),
    path('schedule/<int:pk>/', ScheduleDetailAPIView.as_view()),
    path('comment/post/', CommentCreateAPIView.as_view()),
    path('comment/<int:pk>/', CommentDetailAPIView.as_view())
]
