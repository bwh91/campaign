from django.db import models
from django.template.defaultfilters import slugify
from django.core.urlresolvers import reverse

class Head(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title

class Footer(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title

class Sidebar(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title

class Hero(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title

class Header(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title


class Campaign(models.Model):
    title = models.CharField(max_length=50)
    body = models.TextField(blank=True, null=True)
    head = models.ForeignKey(Head, blank=True, null=True)
    header = models.ForeignKey(Header, blank=True, null=True)
    hero = models.ForeignKey(Hero, blank=True, null=True)
    footer = models.ForeignKey(Footer, blank=True, null=True)
    sidebar = models.ForeignKey(Sidebar, blank=True, null=True)
    slug = models.SlugField(default='', blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        kwargs = {
                'slug': self.slug,
                }
        return reverse('campaign_view', kwargs=kwargs)
