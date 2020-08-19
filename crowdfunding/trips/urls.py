from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .import views

urlpatterns = [
    path('trips/', views.TripList.as_view()),
    path('trip-detail/', views.TripDetail.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)

