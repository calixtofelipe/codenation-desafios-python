from django.core.validators import MinLengthValidator, EmailValidator, validate_ipv4_address
from django.db import models
# from datetime import datetime, timedelta
import datetime
# Create your models here.
LEVEL_CHOICES = [
    ('critical', 'critical.'),
    ('debug', 'debug'),
    ('error', 'error'),
    ('warning', 'warning'),
    ('information', 'info'),
]

min_validator = MinLengthValidator(8, 'the password cant be small then 8')

class UserManager(models.Manager):
    def get_admin_users(self):
        queryset = User.objects.raw('SELECT u.* FROM api_user u, \
         api_user_group ug, api_group g where u.id=ug.user_id and  \
         ug.group_id=g.id and g.name = "admin" order by u.name')
        return queryset

    def get_active_users(self):
        dt = datetime.now()
        d_truncated = datetime.datetime.date(dt.year, dt.month, dt.day)
        date_filter = d_truncated-datetime.timedelta(days=10)
        queryset = User.objects.raw('SELECT * FROM api_user u \
        where u.last_login >=%s  order by u.name', [date_filter])
        return queryset
    
    def get_amount_users(self):
        # queryset = User.objects.raw('SELECT 1 as id, COUNT(*) as qtduser FROM api_user u')
        # queryset.qtduser
        return User.objects.count()

class EventManager(models.Manager):
    def get_all_debug_events(self):
        queryset = Event.objects.raw('SELECT * FROM api_event where level= "debug" ')
        return queryset
    
    def get_all_critical_events_by_user(self, user):
        queryset = Event.objects.raw('SELECT e.* FROM api_event e, api_user u, api_agent a \
            where a.user_id=u.id and e.agent_id=a.id and e.level="critical" and a.user_id=%s', [user.id])
        return queryset

class AgentManager(models.Manager):
    def get_all_agents_by_user(self, username):
        queryset = Agent.objects.raw('SELECT a.* FROM api_user u, api_agent a \
            where a.user_id=u.id and u.name=%s', [username])
        return queryset


class GroupManager(models.Manager):
    def get_all_events_by_group(self):
        queryset = Event.objects.raw('SELECT g.* FROM api_event e, api_user u,api_group g, \
        api_user_group ug, api_agent a \
        where a.user_id=u.id and e.agent_id=a.id and e.level="information" \
        and u.id=ug.user_id and g.id=ug.group_id')
        return queryset

class Group(models.Model):
    objects = GroupManager()
    name = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class User(models.Model):
    objects = UserManager()
    name = models.CharField(max_length=50)
    email = models.EmailField(validators=[EmailValidator], null=True)
    password = models.CharField(max_length=50, validators=[min_validator])
    last_login = models.DateField(default=datetime.date.today)
    group = models.ManyToManyField(Group)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class Agent(models.Model):
    name = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.PROTECT, null=True)
    address = models.GenericIPAddressField(validators=[validate_ipv4_address], null=True)
    status = models.BooleanField(default=False)
    env = models.CharField(max_length=20)
    version = models.CharField(max_length=5)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class Event(models.Model):
    objects = EventManager()
    level = models.CharField(max_length=20, choices=LEVEL_CHOICES)
    data = models.TextField(max_length=500)
    agent = models.OneToOneField(Agent, on_delete=models.PROTECT)
    arquivado = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.level +' in ' + self.agent.name

    class Meta:
        ordering = ['date']


