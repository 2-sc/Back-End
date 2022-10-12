from django.urls import path
from .views import StopWatchView, TotalView

urlpatterns = [
    path('total/', TotalView.as_view()),
    path('start/', StopWatchView.as_view()),
    path('end/<int:pk>/', StopWatchView.as_view())
]
