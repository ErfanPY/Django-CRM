from django.contrib import admin
from organizations.models import Organization, OrganizationProduct, Opportunity, Report

admin.site.register([Organization, OrganizationProduct, Opportunity, Report])
