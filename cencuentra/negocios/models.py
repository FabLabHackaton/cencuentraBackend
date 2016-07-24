from django.core.validators import RegexValidator
from django.db import models

CHOICES_TYPE =(
    ('C','Comida'),
    ('ET','Electronica y Tecnologia'),
    ('RA','Ropa y Accesorios'),
    ('M', 'Musica'),
    ('E', 'Entretenimiento'),
    ('O', 'Otros')
)


# Create your models here.
class Negocio(models.Model):
    class meta():
        verbose_name = 'Negocio'
        verbose_name_plural = 'Negocios'

    #Fields
    email = models.EmailField(
        'email',
        blank=False
    )
    name = models.CharField(
        'name',
        max_length=255,
        blank=False,
        unique=True,
        error_messages={
            'unique': "El nombre de usuario ya existe",
        },
    )

    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{10,15}$',
        message="El numero tiene que tener este formato '55-5555-5555'."
    )
    phone_Number = models.CharField(
        'phone number',
        validators=[phone_regex],
        blank=False,
        max_length=13,
        )

    lat = models.CharField(
        'lat',
        max_length=500,
    )
    long = models.CharField(
        'long',
        max_length=500,
    )
    type = models.CharField(
        'type',
        max_length=255,
        choices= CHOICES_TYPE
    )

    opening = models.TimeField(
        'opening',
    )
    closing = models.TimeField(
        'closing',
    )

    def __str__(self):
        return self.name

