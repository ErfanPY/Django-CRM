from rest_framework import viewsets, permissions
from products.serializers import ProductSerializer

from products.models import Product


class ProductsViewSet(viewsets.ModelViewSet):
    """
        A model viewset for Products model.
    """
    
    queryset = Product.objects.all().order_by('-name')
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ProductSerializer
