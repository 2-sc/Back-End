from django.urls import path
from .views import TodoAPIView, TodoCreateAPIView, TodoDetailAPIView, ScheduleAPIView, ScheduleCreateAPIView, \
    ScheduleDetailAPIView, CommentAPIView, CommentCreateAPIView, CommentDetailAPIView

urlpatterns = [
    # path('all/', CommentAPIView.as_view()),
    path('todo/', TodoAPIView.as_view()),
    path('todo/post/', TodoCreateAPIView.as_view()),
    path('todo/<int:pk>/', TodoDetailAPIView.as_view()),
    path('schedule/', ScheduleAPIView.as_view()),
    path('schedule/post/', ScheduleCreateAPIView.as_view()),
    path('schedule/<int:pk>/', ScheduleDetailAPIView.as_view()),
    path('comment/', CommentAPIView.as_view()),
    path('comment/post/', CommentCreateAPIView.as_view()),
    path('comment/<int:pk>/', CommentDetailAPIView.as_view()),
]
