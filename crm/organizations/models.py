from django.db import models
from django.utils.translation import ugettext_lazy as _

        
class OrganizationProduct(models.Model):
    name = models.CharField(max_length=50, verbose_name=_('محصول مشتری'))
    related_products = models.ManyToManyField('products.Product', verbose_name=_('محصولات مرتبط'))

    class Meta:
        ordering = ('name',)
        verbose_name = _('محصول ارگان')
        verbose_name_plural = _('محصولات ارگان')

    def __str__(self):
        return self.name

        
class Organization(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name=_('نام'))
    province = models.CharField(max_length=50, verbose_name=_('استان'))
    phone_number = models.CharField(max_length=20, unique=True, verbose_name=_('شماره تلفن'))
    workers_count = models.PositiveIntegerField(verbose_name=_('تعداد کارگران'))
    contact_fullname = models.CharField(max_length=50, verbose_name=_('نام مخاطب'))
    contact_phone_number = models.CharField(max_length=20, verbose_name=_('شماره تلفن مخاطب'))
    email = models.EmailField(unique=True, verbose_name=_('ایمیل'))
    create_date = models.DateField(auto_now_add=True, verbose_name=_('تاریخ ثبت'))
    registrar = models.ForeignKey('auth.User', on_delete=models.PROTECT, verbose_name=_('کارشناس فروش'))
    products = models.ManyToManyField(OrganizationProduct, verbose_name=_('محصولات'))

    class Meta:
        ordering = ('name',)
        verbose_name = _('ارگان')
        verbose_name_plural = _('ارگان ها')

    def __str__(self):
        return self.name


class Opportunity(models.Model):
    create_date = models.DateField(auto_now_add=True, verbose_name=_('تاریخ ثبت'))
    last_modified_date = models.DateField(auto_now=True, verbose_name=_('تاریخ آخرین پیگیری'))
    organization = models.ForeignKey(Organization, on_delete=models.PROTECT, verbose_name=_('ارگان طرف حساب'))
    sales_people = models.ManyToManyField('auth.user', verbose_name=_('کارشناسان فروش'))
    # status
    class Meta:
        ordering = ('last_modified_date',)
        verbose_name = _('موقعیت')
        verbose_name_plural = _('موقعیت ها')

    def __str__(self):
        return str(self.organization) + " _ " + str(self.sales_people)


class Report(models.Model):
    text = models.TextField(verbose_name=_('گزارش کار'))
    create_date = models.DateField(auto_now_add=True, verbose_name=_('تاریخ ثبت'))
    creator = models.ForeignKey('auth.User', on_delete=models.PROTECT, verbose_name=_('کارشناس فروش'))
    opportunity = models.ForeignKey(Opportunity, on_delete=models.PROTECT, verbose_name=_('موقعیت فروش'))

    class Meta:
        ordering = ('create_date',)
        verbose_name = _('گزارش')
        verbose_name_plural = _('گزارش ها')

    def __str__(self):
        return str(self.opportunity) + " _ " + str(self.creator)
