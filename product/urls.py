from django.urls import path
from .views import EventView,EventThumbnailView

urlpatterns=[
    path('event/',EventView.as_view()),
    #이메일 url
    path('thumbnail/<obj_id>/',EventThumbnailView.as_view()),
]