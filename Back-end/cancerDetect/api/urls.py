from posixpath import basename
from django.db import router
from django.urls import path,include
from .views import *
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register('cancerdetect',CancerDetectViewSet,basename='cancerdetect')
# router.register('cancerDetail',CancerDetailViewSet,basename='cancerDetail')

urlpatterns = [
    path('', include(router.urls)),#post
]