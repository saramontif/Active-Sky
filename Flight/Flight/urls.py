from django.urls import path

from core.views import phon_scan
from core.views.active_main_window import active_view
from core.views.main_first_window import home_view


urlpatterns = [
    path('phone_scan/', phon_scan.scan, name='phon_scan'),
    path('start/', home_view.as_view(), name='start'),
    path('active/', active_view.as_view(), name='active_window'),
]
