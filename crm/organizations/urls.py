from django.urls import include, path
from rest_framework import routers
from organizations import api

router = routers.DefaultRouter()
router.register(r'api', api.OrganizationsViewSet, basename='Organization')

urlpatterns = [
    path('', include(router.urls)),
]