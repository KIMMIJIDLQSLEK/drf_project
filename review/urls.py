from django.urls import path
from .views import ReviewGetOrCreateView


urlpatterns=[
    path('',ReviewGetOrCreateView.as_view()),
]