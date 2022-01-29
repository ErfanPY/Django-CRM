from django import forms

from follow_up import models


class FollowUpsForm(forms.ModelForm):
    """
        A model form for FollowUp model
    """
    
    class Meta:
        model = models.FollowUp
        fields = [
            'organization',
            'text',
        ]
