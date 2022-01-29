from django.urls import path
from web.views import create_organizations_view, home, list_organizations_view, retrieve_organizations_view, edit_organizations_view

app_name = 'web'

urlpatterns = [
    path('organizations/create/', create_organizations_view, name='create-organizations'),
    path('organizations/list/', list_organizations_view, name='list-organizations'),
    path('organizations/retrieve/<int:pk>/', retrieve_organizations_view, name='retrieve-organizations'),
    path('organizations/edit/<int:pk>/', edit_organizations_view, name='edit-organizations'),
    path('', home, name='home'),
]
