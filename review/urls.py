from django.urls import path
from .views import ReviewGetOrCreateView,ReviewUpdateView


urlpatterns=[
    path('',ReviewGetOrCreateView.as_view()),
    path('<obj_id>/update/',ReviewUpdateView.as_view()),
]