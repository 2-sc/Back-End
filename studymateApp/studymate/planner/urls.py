from django.urls import path
from .views import ScheduleAPIView #, TodoAPIView
from .views import TodoCreateAPIView, TodoDetailAPIView, ScheduleCreateAPIView, ScheduleDetailAPIView

urlpatterns = [
    path('all/', ScheduleAPIView.as_view()),
    path('todo/post/', TodoCreateAPIView.as_view()),
    path('todo/<int:pk>/', TodoDetailAPIView.as_view()),
    path('schedule/post/', ScheduleCreateAPIView.as_view()),
    path('schedule/<int:pk>/', ScheduleDetailAPIView.as_view()),
]
