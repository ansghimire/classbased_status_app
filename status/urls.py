from django.urls import path
from .views import StatusCreateView, StatusDeleteView, StatusUpdateView

urlpatterns = [
    path('create/', StatusCreateView.as_view(), name="create"),
    path('delete/<int:pk>/', StatusDeleteView.as_view(), name="delete"),
    path('update/<int:pk>/', StatusUpdateView.as_view(), name="update")
]