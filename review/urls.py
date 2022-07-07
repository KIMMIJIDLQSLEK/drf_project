from django.urls import path
from .views import ReviewGetOrCreateView,ReviewUpdateView,ReviewDeleteView


urlpatterns=[
    path('',ReviewGetOrCreateView.as_view()),
    path('<obj_id>/update/',ReviewUpdateView.as_view()),
    path('<obj_id>/delete/',ReviewDeleteView.as_view()),
]