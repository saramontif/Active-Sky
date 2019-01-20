from django.contrib import admin
from django.urls import path

from app import views
from app.views import main_first_window
from app.views import active_main_window

from . import view
from app.views import *

urlpatterns = [
    path('<int:question_id>/', view.detail, name='detail'),
    path('start/', main_first_window.open_window, name='open_window'),
    path('active/', active_main_window.active_window, name='active_window'),

]


