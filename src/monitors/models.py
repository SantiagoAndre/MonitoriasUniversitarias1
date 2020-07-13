from django.db import models
from django.db.models import CASCADE

# Create your models here.


class College(models.Model):
    """Universidad"""

    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Career(models.Model):
    """Carrerra"""

    name = models.CharField(max_length=200)
    description = models.TextField(null=True)

    college = models.ForeignKey(
        'College', related_name='careers', on_delete=CASCADE)

    def __str__(self):
        return self.name


class City(models.Model):
    """Ciudad"""

    name = models.CharField(max_length=45)

    def __str__(self):
        return self.name


class Contact(models.Model):
    """Contacto"""

    address = models.CharField(max_length=200)
    phone = models.BigIntegerField()
    family_phone = models.BigIntegerField()

    city = models.ForeignKey(
        'City', related_name='contacts', on_delete=CASCADE)

    def __str__(self):
        return self.address


class Monitor(models.Model):
    """Monitor"""

    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField()
    semester = models.IntegerField()

    contact = models.OneToOneField('Contact', on_delete=CASCADE)
    careers = models.ManyToManyField('Career', related_name='monitors')

    def __str__(self):
        return self.name


class Service(models.Model):
    """Servicio"""

    name = models.CharField(max_length=200)
    description = models.TextField(null=True)

    monitor = models.ForeignKey(
        'Monitor', related_name='services', on_delete=CASCADE)

    def __str__(self):
        return self.name


class Skill(models.Model):
    """Habilidades"""

    name = models.CharField(max_length=100)

    monitors = models.ManyToManyField('Monitor', related_name='skills')

    def __str__(self):
        return self.name


class Client(models.Model):
    """Cliente"""

    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField()

    def __str__(self):
        return self.name


class Quoation(models.Model):
    """Cotizacion"""

    # TODO: define field file
    acepted = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    expiration = models.DateTimeField()
    delivery = models.DateTimeField()
    price = models.IntegerField()

    monitor = models.ForeignKey('Monitor', related_name='quoations', on_delete=CASCADE)
    client = models.ForeignKey('Client', related_name='quoations', on_delete=CASCADE)
