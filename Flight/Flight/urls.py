from django.urls import path

from core.views.active_main_window import Active_view
from core.views.phone_scan import ScanView
from core.views.main_first_window import HomeView, FlagView

urlpatterns = [
    path('phone_scan/', ScanView.as_view(), name='phone_scan'),
    path('start/', HomeView.as_view(), name='start'),
    path('active/', Active_view.as_view(), name='active_window'),
    path('api/flag/', FlagView.as_view(), name='flag'),
]
