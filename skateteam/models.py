from django.db import models

# two custon models for new app - code inspired by CI Boutique-ado project


class Teamcat(models.Model):

    """
    Model Teamcat to categorise skaters on the website.
    """

    class Meta:
        verbose_name_plural = 'Teamcat'  # changes the name of the models in django server

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Skateteam(models.Model):
    """
    Model Skateteam to gather required information to create
    a memeber as an item on the site.
    """

    teamcat = models.ForeignKey(
        'Teamcat', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    rating = models.DecimalField(
        max_digits=6, decimal_places=2, null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name


# Create your models here.
