from django.urls import path
from .views import *

urlpatterns = [
    path('api/v1/list/', URLsListView.as_view()),
    path('api/v1/create/', URLsCreateView.as_view()),
    path('api/v1/list/<int:pk>/', URLsDetailView.as_view()),
    path('short/<str:short_url>/', URLsShortView.as_view()),
]
