from django.urls import include, path
from rest_framework import routers
from follow_up.views import (
    create_follow_ups_view,
    list_follow_ups_view,
)
from follow_up.api import FollowUpViewSet

app_name = "follow_up"

router = routers.DefaultRouter()
router.register(r'', FollowUpViewSet, basename='FollowUp')

urlpatterns = [
    path('api/', include(router.urls)),
    path('create/', create_follow_ups_view, name='create-follow-up'),
    path('list/', list_follow_ups_view, name='list-follow-ups'),
]
