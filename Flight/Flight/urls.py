from django.contrib import admin
from django.urls import path
from . import view

urlpatterns = [
    path('<int:question_id>/', view.detail, name='detail'),
    path('phone_scan/', view.phon_scan, name='phon_scan'),

]