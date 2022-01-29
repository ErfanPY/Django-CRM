from django.urls import include, path
from rest_framework import routers
from products import api

router = routers.DefaultRouter()
router.register(r'api', api.ProductsViewSet)

urlpatterns = [
    path('', include(router.urls)),
]