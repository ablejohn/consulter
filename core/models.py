from django.db import models
from django.utils.translation import gettext_lazy as _


class AbstractTimeStampModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class OurServices(AbstractTimeStampModel):
    icon = models.CharField(_("Fa Icon"), max_length=15)
    title = models.CharField(_("Title"), max_length=30)
    image = models.ImageField(_("Image"), upload_to="media/services")
    description = models.TextField(_("Short Description"))

    class Meta:
        verbose_name = "Our Service"
        verbose_name_plural = "Our Services"

    def __str__(self):
        return self.title


class ContactMessages(AbstractTimeStampModel):
    name = models.CharField(_("Name"), max_length=60)
    email = models.EmailField(_("Email"))
    subject = models.CharField(_("Subject"), max_length=60)
    message = models.TextField(_("Message"))

    class Meta:
        verbose_name = "Contact Message"
        verbose_name_plural = "Contact Messages"

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.name = str(self.name).upper()
        return super().save(*args, **kwargs)
