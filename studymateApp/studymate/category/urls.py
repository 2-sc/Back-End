from django.urls import path
from .views import CategoryView, CategoryAllView

urlpatterns = [
    path('all/', CategoryAllView.as_view()),
    path('post/', CategoryView.as_view()),
    path('<int:pk>/', CategoryView.as_view())
]