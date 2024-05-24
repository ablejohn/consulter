from django.db import models
from core.models import AbstractTimeStampModel
from django.utils.translation import gettext_lazy as _
from tinymce import models as tinymce_models
from django.urls import reverse


class PostTag(AbstractTimeStampModel):
    name = models.CharField(_("Tag Name"), max_length=20)

    def __str__(self):
        return self.name


class Post(AbstractTimeStampModel):
    image = models.ImageField(_("Image"), upload_to="blog/posts")
    title = models.CharField(_("Title"), max_length=60)
    content = tinymce_models.HTMLField(_("Content"))
    tags = models.ManyToManyField(PostTag, verbose_name="Post Tags")

    def get_absolute_url(self):
        return reverse("blog:detail", kwargs={"id": self.pk})

    def __str__(self):
        return self.title
