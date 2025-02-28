from django.urls import path
from .views import HomePageView, RegisterFlightView, ListFlightsView, StatisticsView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('flights/register', RegisterFlightView.as_view(), name='register_flight'),
    path('flights/list', ListFlightsView.as_view(), name='list_flights'),
    path('flights/statistics', StatisticsView.as_view(), name='statistics'),
]