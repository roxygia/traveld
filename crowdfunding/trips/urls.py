from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .import views

urlpatterns = [
    path('trips/', views.TripList.as_view()),
    path('trips/<int:pk>', views.TripDetail.as_view()),
    path('trips-detail/<int:pk>', views.TripDetail.as_view()),
    path('pledges/', views.PledgeList.as_view()),
    path('pledges/<int:pk>', views.PledgeDetail.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)

