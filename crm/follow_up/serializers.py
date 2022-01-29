from rest_framework import serializers
from follow_up.models import FollowUp


class FollowUpSerializer(serializers.ModelSerializer):
    """
        A model serializer for FollowUp model
    """
    
    organization_name = serializers.CharField(source='organization.name', required=False)

    class Meta:
        model = FollowUp
        read_only_fields = [
            'pk',
            'creator',
            'create_date',
        ]
        
        fields = [
            'pk',
            'create_date',
            'creator',
            'text',
            'organization',
            'organization_name',
        ]
