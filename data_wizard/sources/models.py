from django.db import models
from django.utils.translation import gettext_lazy as _


class FileSource(models.Model):
    name = models.CharField(_('Name'), max_length=255,
        null=True, blank=True)
    file = models.FileField(_('File'), upload_to='datawizard/')
    date = models.DateTimeField(_('Date'), auto_now_add=True)

    def __str__(self):
        return self.name or self.file.name


class URLSource(models.Model):
    name = models.CharField(_('Name'), max_length=255, null=True, 
        blank=True)
    url = models.URLField(_('URL'),)
    date = models.DateTimeField(_('Date'), auto_now_add=True)

    def __str__(self):
        return self.name or self.url
