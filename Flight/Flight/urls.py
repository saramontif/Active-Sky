from django.urls import path
from app.views import main_first_window, phon_scan, active_main_window
from app.views.main_first_window import home_view
from . import view



urlpatterns =[
    path('phone_scan/', phon_scan.scan, name='phon_scan'),
    path('start/', home_view.as_view(), name='start'),
    path('active/', active_main_window.active_window, name='active_window'),
]

