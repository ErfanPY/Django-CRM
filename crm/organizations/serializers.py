from rest_framework import serializers
from organizations.models import Organization

# class OrganizationSerializer(serializers.HyperlinkedModelSerializer):
class OrganizationSerializer(serializers.ModelSerializer):
    """
        A model serializer for Organization model
    """
    
    registrar_name = serializers.CharField(source='registrar.username', required=False)

    class Meta:
        model = Organization
        read_only_fields = (
            'pk',
            'registrar',
            'create_date',
        )
        fields = [
            'pk',
            'name',
            'province',
            'phone_number',
            'workers_count',
            'contact_fullname',
            'contact_phone_number',
            'email',
            'products',
            'registrar',
            'registrar_name',
            'create_date'
        ]

