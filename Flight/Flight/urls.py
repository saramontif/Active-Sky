from django.contrib import admin
from django.urls import path
from . import view

urlpatterns = [
    path('<int:question_id>/', view.detail, name='detail'),


]