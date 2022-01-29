from django.db import models
from django.utils.translation import ugettext_lazy as _


class FollowUp(models.Model):
    create_date = models.DateField(auto_now_add=True, verbose_name=_('تاریخ ثبت'))
    creator = models.ForeignKey('auth.User', on_delete=models.PROTECT, verbose_name=_('کارشناس فروش'))
    organization = models.ForeignKey('organizations.Organization', on_delete=models.PROTECT, verbose_name=_('ارگان'))
    text = models.TextField(verbose_name='متن پیگیری فروش')

    class Meta:
        ordering = ('create_date',)
        verbose_name = _('پیگیری فروش')
        verbose_name_plural = _('پیگیری های فروش')

    def __str__(self):
        return str(self.organization) + " _ " + str(self.creator)
