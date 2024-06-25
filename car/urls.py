from django.urls import path
from .views import CarApiView

urlpatterns = [
    path('api/v1/car/',CarApiView.as_view()),
    # path('api/v1/car/<int:pk>/',CarDetailApiView.as_view())
]