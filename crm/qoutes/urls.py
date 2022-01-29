from django.urls import include, path
from rest_framework import routers
from qoutes.views import (
    create_qoutes_view,
    list_qoutes_view,
    send_email_view,
    pdf_view
)
from qoutes.api import (
    QouteViewSet,
    QouteProductDetailViewSet,
)

app_name = "qoutes"

router = routers.DefaultRouter()
router.register(r'qoute', QouteViewSet, basename='Qoute')
router.register(r'product', QouteProductDetailViewSet, basename='QouteProductDetail')

urlpatterns = [
    path('api/', include(router.urls)),
    path('create/', create_qoutes_view, name='create-qoutes'),
    path('list/', list_qoutes_view, name='list-qoutes'),
    path('send_email/<int:pk>', send_email_view, name='send-email'),
    path('pdf/<int:pk>', pdf_view, name='pdf'),
]
