from rest_framework import serializers
from products.models import Product


class ProductSerializer(serializers.ModelSerializer):
    """
        A model serializer for Product model
    """
    
    class Meta:
        model = Product
        fields = [
            'name',
            'price',
            'includes_taxes',
            'catalog_pdf_file',
            'catalog_image_file',
            'technical_features' 
        ]
