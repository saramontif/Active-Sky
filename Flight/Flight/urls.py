from django.urls import path

from core.views import active_main_window
from core.views import phon_scan
from core.views.main_first_window import home_view



urlpatterns =[
    path('phone_scan/', phon_scan.scan, name='phon_scan'),
    path('start/', home_view.as_view(), name='start'),
    path('active/', active_main_window.active_window, name='active_window'),
]

