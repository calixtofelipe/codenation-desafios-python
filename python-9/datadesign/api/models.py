from django.db import models
from django.core.validators import MinLengthValidator


class Agent(models.Model):
    name = models.CharField('name', max_length=50)
    status = models.BooleanField('status')
    env = models.CharField('env', max_length=20)
    version = models.CharField('version', max_length=5)
    address = models.GenericIPAddressField(
        'address', protocol='IPV4', max_length=39)

    def __str__(self):
        return self.name


class User(models.Model):
    name = models.CharField('name', max_length=50)
    last_login = models.DateTimeField(
        'last_login', blank=True, auto_now=True)  # blank=True,
    email = models.EmailField('email', max_length=254)
    password = models.CharField(
        'password', max_length=50,
        validators=[MinLengthValidator(8)])

    def __str__(self):
        return self.name


class Group(models.Model):
    name = models.CharField('name', max_length=50)

    def __str__(self):
        return self.name


class Event(models.Model):
    class EventChoices(models.TextChoices):
        CRITICAL = 'CRITICAL'
        DEBUG = 'DEBUG'
        ERROR = 'ERROR'
        WARNING = 'WARNING'
        INFO = 'INFO'

    level = models.CharField('level', max_length=20,
                             choices=EventChoices.choices)
    data = models.TextField('data')
    arquivado = models.BooleanField('arquivado')
    date = models.DateField('date', blank=True, auto_now=True)
    agent = models.ForeignKey(
        Agent,
        on_delete=models.deletion.DO_NOTHING,
        # related_name='Agent'
    )
    user = models.ForeignKey(
        User,
        on_delete=models.deletion.DO_NOTHING,
        #  related_name='User'
    )


class GroupUser(models.Model):
    group = models.ForeignKey(
        Group,
        on_delete=models.deletion.DO_NOTHING,
        related_name='group'
    )
    user = models.ForeignKey(
        User,
        on_delete=models.deletion.DO_NOTHING,
        #  related_name='User'
    )
