from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _


# simple aurther user model
class Auther(AbstractUser):
    email = models.EmailField(
        _("email address"),
        unique=True,
        blank=True,
    )
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []


class News(models.Model):
    aurther = models.ForeignKey(Auther, on_delete=models.CASCADE)
    heading = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(
        _("date joined"),
        auto_now_add=True,
    )
    last_upadted = models.DateTimeField(
        verbose_name=_("last updated"),
        auto_now=True,
    )
