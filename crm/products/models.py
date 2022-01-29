from django.db import models
from django.utils.translation import ugettext_lazy as _

class Product(models.Model):
    name = models.CharField(max_length=50, verbose_name=_('نام محصول'))
    price = models.PositiveIntegerField(verbose_name=_('قیمت محصول'))
    includes_taxes = models.BooleanField(verbose_name=_('آیا مشمول مالیات است ؟'))
    catalog_pdf_file = models.FileField(upload_to="pdfs/", null=True, blank=True, verbose_name=_('پی دی اف کاتالوگ'))
    catalog_image_file = models.ImageField(upload_to="images/", null=True, blank=True, verbose_name=_('تصویر کاتالوگ'))
    technical_features = models.TextField(verbose_name=_('ویژگی های فنی'))

    class Meta:
        ordering = ('name',)
        verbose_name = _('محصول')
        verbose_name_plural = _('محصول ها')

    def __str__(self):
        return self.name