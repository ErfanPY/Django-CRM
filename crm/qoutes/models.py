from enum import unique
from django.db import models
from django.utils.translation import ugettext_lazy as _


class Qoute(models.Model):
    create_date = models.DateField(auto_now_add=True, verbose_name=_('تاریخ ثبت'))
    creator = models.ForeignKey('auth.User', on_delete=models.PROTECT, verbose_name=_('کارشناس فروش'))
    organization = models.ForeignKey('organizations.Organization', on_delete=models.PROTECT, verbose_name=_('ارگان'))


    class Meta:
        ordering = ('create_date',)
        verbose_name = _('پیش فاکتور')
        verbose_name_plural = _('پیش فاکتور ها')

    def __str__(self):
        return str(self.organization) + " _ " + str(self.creator)

    def get_total_products_price(self):
        total_products_price = 0
        
        for prod in self.qouteproductdetail_set.all():
            total_products_price += prod.calculate_total_price()

        return total_products_price

    def get_total_qty(self):
        total_qty = 0
        
        for prod in self.qouteproductdetail_set.all():
            total_qty += prod.qty

        return total_qty


class QouteProductDetail(models.Model):
    product = models.ForeignKey('products.Product', on_delete=models.PROTECT, verbose_name=_('محصول'))
    qty = models.PositiveIntegerField(verbose_name=_('تعداد'))
    price = models.PositiveIntegerField(verbose_name=_('قیمت'))
    discount_percent = models.PositiveIntegerField(verbose_name=_('درصد تخفیف'))
    qoute = models.ForeignKey(Qoute, on_delete=models.PROTECT, verbose_name=_('پیش فاکتور'))

    class Meta:
        ordering = ('price',)
        verbose_name = _('جزئیات محصول پیش فاکتور')
        verbose_name_plural = _('جزئیات محصولات پیش فاکتور')

    def __str__(self):
        return str(self.qoute) + " _ " + str(self.product)

    def calculate_total_price(self):
        total_price = self.price * self.qty
        total_price -= total_price * (self.discount_percent / 100)
        
        if self.product.includes_taxes:
            total_price += total_price / 10

        return total_price

email_status_choise = [
    ['شکست', 'ارسال ایمیل شکست خورد.'], 
    ['موفقیت', 'ارسال ایمیل موفقیت امیز بود.']
]

class Emails(models.Model):
    reciver = models.CharField(max_length=50, verbose_name='ایمیل دریافت کننده')
    status = models.CharField(max_length=6, verbose_name="وضعیت ارسال", choices=email_status_choise)
    send_date = models.DateField(verbose_name="تاریخ ارسال ایمیل", auto_now_add=True)
    sender = models.ForeignKey('auth.user', on_delete=models.CASCADE, verbose_name='کاربر ارسال کننده')
    class Meta:
        ordering = ('send_date',)
        verbose_name = _('ایمیل')
        verbose_name_plural = _('ایمیل ها')

    def __str__(self):
        return str(self.reciver) + " _ " + str(self.sender.username)
