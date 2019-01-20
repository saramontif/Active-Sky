
from django.urls import path

from core.views import active_main_window
from core.views.phone_scan import scan
from core.views.main_first_window import home_view




urlpatterns =[
    path('phone_scan/', scan.as_view(), name='phone_scan'),
    path('start/', home_view.as_view(), name='start'),
    path('active/', active_main_window.active_window, name='active_window'),
]
