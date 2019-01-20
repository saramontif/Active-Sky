from django.contrib import admin
from django.urls import path

from app import views
from app.views import main_first_window
from . import view
from app.views import *

urlpatterns = [
    path('start/', main_first_window.open_window, name='open_window'),

]


