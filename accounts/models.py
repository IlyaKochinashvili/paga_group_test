from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.utils.translation import ugettext_lazy as _

from accounts import managers


class Account(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'), max_length=255,
                              unique=True, db_index=True)
    is_staff = models.BooleanField(
        _('staff status'), default=False, help_text=_(
            'Designates whether the user can log into this admin site.'))
    is_active = models.BooleanField(_('active'), default=True, help_text=_(
        'Designates whether this user should be treated as '
        'active. Unselect this instead of deleting accounts.'))
    objects = managers.UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        db_table = 'account'
        verbose_name = _('account')
        verbose_name_plural = _('accounts')


class Profile(models.Model):
    user = models.OneToOneField('Account', on_delete=models.CASCADE)
    username = models.CharField(max_length=30, unique=True)
    first_name = models.CharField(_('first name'), max_length=30, blank=True)
    last_name = models.CharField(_('last name'), max_length=30, blank=True)
    date_of_birth = models.DateField(_('date_of_birth'), null=True, blank=True)
    objects = models.Manager()

    def __str__(self):
        return self.username
