from django.urls import path

from core.views.active_main_window import active_view
from core.views.phone_scan import ScanView
from core.views.main_first_window import home_view




urlpatterns =[
    path('phone_scan/', ScanView.as_view(), name='phone_scan'),
    path('start/', home_view.as_view(), name='start'),
    path('active/', active_view.as_view(), name='active_window'),
]
