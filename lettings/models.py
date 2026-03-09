from django.core.validators import MaxValueValidator
from django.core.validators import MinLengthValidator
from django.db import models


class Address(models.Model):
    """
    Model representing a postal address.

    :@var number: PositiveIntegerField, street number (max 4 digits)
    :@var street: CharField, street name (max 64 chars)
    :@var city: CharField, city name (max 64 chars)
    :@var state: CharField, state code (2 chars)
    :@var zip_code: PositiveIntegerField, postal code (max 5 digits)
    :@var country_iso_code: CharField, ISO country code (3 chars)
    """
    number = models.PositiveIntegerField(validators=[MaxValueValidator(9999)])
    street = models.CharField(max_length=64)
    city = models.CharField(max_length=64)
    state = models.CharField(max_length=2, validators=[MinLengthValidator(2)])
    zip_code = models.PositiveIntegerField(validators=[MaxValueValidator(99999)])
    country_iso_code = models.CharField(max_length=3, validators=[MinLengthValidator(3)])

    def __str__(self):
        """
        Return a readable string representation of the address.

        @return: A string of the form 'number street'
        @rtype: str
        """
        return f'{self.number} {self.street}'

    class Meta:
        db_table = 'oc_lettings_site_address'
        verbose_name_plural = "addresses"


class Letting(models.Model):
    """
    Model representing a rental property (letting).

    :@var title: CharField, title of the letting (max 256 chars)
    :@var address: OneToOneField, linked Address instance
    """
    title = models.CharField(max_length=256)
    address = models.OneToOneField(Address, on_delete=models.CASCADE)

    def __str__(self):
        """
        Return the title of the letting.

        @return: Title of the letting
        @rtype: str
        """
        return self.title

    class Meta:
        db_table = 'oc_lettings_site_letting'
