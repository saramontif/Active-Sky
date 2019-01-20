from django.contrib import admin
from django.urls import path
from Flight import view

urlpatterns = [
    path('<int:question_id>/', view.detail, name='detail'),
    path('<int:question_id>/', view.detail, name='detail'),

]