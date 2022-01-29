from rest_framework import serializers
from qoutes.models import Qoute, QouteProductDetail


class QouteSerializer(serializers.ModelSerializer):
    """
        A model serializer for Qoute model
    """
    
    organization_name = serializers.CharField(source='organization.name', required=False)
    total_products_price = serializers.SerializerMethodField()
    products_text = serializers.SerializerMethodField()

    def get_total_products_price(obj, self):
        return self.get_total_products_price()

    def get_products_text(obj, self):
        products_text_temp = ""
        
        products = self.qouteproductdetail_set.all()
        products_text_temp = ", ".join([prod.product.name for prod in products])
        
        return products_text_temp

    class Meta:
        model = Qoute
        read_only_fields = ['pk']
        fields = [
            'pk',
            'create_date',
            'creator',
            'organization',
            'organization_name',
            'total_products_price',
            'products_text'
        ]


class QouteProductDetailSerializer(serializers.ModelSerializer):
    """
        A model serializer for QouteProductDetail model
    """
    
    class Meta:
        model = QouteProductDetail
        fields = [
            'product',
            'qty',
            'price',
            'discount_percent',
            'qoute',
            ]
