from rest_framework import permissions, viewsets

from follow_up.models import FollowUp
from follow_up.serializers import FollowUpSerializer


class FollowUpViewSet(viewsets.ModelViewSet):
    """
        A model viewset for FollowUp model.
    """

    permission_classes = [permissions.IsAuthenticated]
    serializer_class = FollowUpSerializer

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)
        return super().perform_create(serializer)

    def get_queryset(self):
        queryset = FollowUp.objects.filter(creator=self.request.user).order_by('-create_date')

        return queryset
