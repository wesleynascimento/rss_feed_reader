from django.db import models
from django.utils.translation import gettext_lazy as _
from apps.accounts.models import User


class Site(models.Model):
    name = models.CharField(
        verbose_name=_('site name'),
        max_length=150,
        unique=True,
        help_text=_('site name'),
    )

    site_url = models.CharField(
        verbose_name=_('site url'),
        max_length=150,
        unique=True,
        help_text=_('site url'),
    )

    category = models.CharField(
        verbose_name=_('caregory'),
        max_length=100,
        unique=True,
        help_text=_('subject of the site'),
    )  # fk pra outra tabela ?

    user_site_relation = models.ManyToManyField(User)

    class Meta:
        verbose_name = _('Site')
        verbose_name_plural = _('Sites')

    def __str__(self):
        return self.name
