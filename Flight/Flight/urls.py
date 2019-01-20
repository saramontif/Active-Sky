from django.urls import path

from core.views import active_main_window
from core.views import phon_scan
# from app.views import main_first_window, phon_scan, active_main_window
from core.views.main_first_window import home_view
# =======
# from app.views import main_first_window, phon_scan, active_main_window
# from app.views.main_first_window import home_view
# from . import view
# >>>>>>> b180b72b76bd6220fece170583882e70eb6cac3c



urlpatterns =[
    path('phone_scan/', phon_scan.scan, name='phon_scan'),
    path('start/', home_view.as_view(), name='start'),
    path('active/', active_main_window.active_window, name='active_window'),
]

