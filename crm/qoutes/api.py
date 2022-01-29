from rest_framework import permissions, viewsets

from qoutes.models import Qoute, QouteProductDetail
from qoutes.serializers import QouteProductDetailSerializer, QouteSerializer


class QouteViewSet(viewsets.ModelViewSet):
    """
        A model viewset for Qoute model.
    """
    
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = QouteSerializer

    def get_queryset(self):
        queryset = Qoute.objects.filter(creator=self.request.user).order_by('-create_date')

        return queryset


class QouteProductDetailViewSet(viewsets.ModelViewSet):
    """
        A model viewset for QouteProductDetail model.
    """
    
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = QouteProductDetailSerializer
    
    def get_queryset(self):
        queryset = QouteProductDetail.objects.filter(qoute__creator=self.request.user).order_by('-product')

        return queryset