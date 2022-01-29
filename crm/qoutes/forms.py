from django import forms

from qoutes import models


class QoutesForm(forms.ModelForm):
    """
        A model form for Qoute model
    """
    
    class Meta:
        model = models.Qoute
        fields = [
            'creator',
            'organization',
        ]


class QouteProductDetailForm(forms.ModelForm):
    """
        A model form for QouteProductDetail model
    """
    
    qoute = forms.IntegerField()

    class Meta:
        model = models.QouteProductDetail
        fields = [
            'product',
            'qty',
            'price',
            'discount_percent',
        ]

