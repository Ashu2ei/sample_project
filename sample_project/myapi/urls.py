# myapi/urls.py
from django.urls import include, path
from rest_framework import routers
from .views import SimplePostAPIView

router = routers.DefaultRouter()

urlpatterns = [
    path('', include(router.urls)),
    path('simple-post/', SimplePostAPIView.as_view(), name='simple-post'),
]
