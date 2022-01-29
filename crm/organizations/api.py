from rest_framework import viewsets, permissions
from organizations.serializers import OrganizationSerializer

from organizations.models import Organization


class OrganizationsViewSet(viewsets.ModelViewSet):
    """
        A model viewset for Organization model.
    """
    
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = OrganizationSerializer

    def perform_create(self, serializer):
        sales_person = self.request.user

        return serializer.save(registrar=sales_person)

    def get_queryset(self):
        queryset = Organization.objects.filter(registrar=self.request.user).order_by('-name')
        return queryset
