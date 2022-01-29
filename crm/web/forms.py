from django import forms

from organizations import models


class OrganizationsForm(forms.ModelForm):

    class Meta:
        model = models.Organization
        fields = [
            'name',
            'province',
            'phone_number',
            'workers_count',
            'contact_fullname',
            'contact_phone_number',
            'email',
            'products',
        ]


# registrar