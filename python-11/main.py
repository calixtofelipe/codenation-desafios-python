from api.models import User, Agent, Event, Group
from datetime import datetime, timedelta
from django.db.models.expressions import RawSQL
from django.db.models import FilteredRelation, Q
from django.db.models import Prefetch


def get_active_users():
    dt = datetime.now()
    dt = dt.replace(hour=0, minute=0, second=0, microsecond=0)
    date_filter = dt-timedelta(days=10)
    # rwqueryset = User.objects.filter(id__in=RawSQL('SELECT u.id FROM api_user u \
    # where u.last_login >=%s  order by u.name', [date_filter]))
    queryset = User.objects.filter(last_login__gte=date_filter)
    return queryset


def get_amount_users() -> User:
    # queryset = User.objects.filter(id__in=RawSQL('SELECT u.id \
    #     FROM api_user u', params=()))
    return User.objects.count()


def get_admin_users() -> User:
    """Traga todos os usuarios com grupo = 'admin'"""
    # queryset = User.objects.filter(id__in='SELECT u.id FROM api_user u, \
    #      api_user_group ug, api_group g where u.id=ug.user_id and  \
    #      ug.group_id=g.id and g.name = "admin" order by u.name')
    queryset = User.objects.filter(group__name='admin')
    return queryset


def get_all_debug_events() -> Event:
    """Traga todos os eventos com tipo debug"""
    # queryset = Event.objects.filter(id__in=RawSQL('SELECT e.id \
    #     FROM api_event e where e.level= "debug" ', params=()))
    queryset = Event.objects.filter(level='debug')
    return queryset


def get_all_critical_events_by_user(agent) -> Event:
    """Traga todos os eventos do tipo critico de um agente específico"""
    # queryset = Event.objects.filter(id__in=RawSQL('SELECT e.id \
    #    FROM api_event e, api_user u, api_agent a \
    #    where a.user_id=u.id and \
    #    e.agent_id=a.id and e.level="critical" and a.id=%s', [agent.id]))
    queryset = Event.objects.filter(level='critical', agent__id=agent.id)
    return queryset


def get_all_agents_by_user(username) -> Agent:
    """Traga todos os agentes de associados a um usuário
    pelo nome do usuário"""
    # queryset = Agent.objects.filter(id__in=RawSQL('SELECT a.id FROM api_user u, api_agent a \
    #         where a.user_id=u.id and u.name=%s', [username]))
    queryset = Agent.objects.filter(user__name=username)
    return queryset


def get_all_events_by_group() -> Group:
    """Traga todos os grupos que contenham alguem que
    possua um agente que possuem eventos do tipo information"""
    # queryset = Group.objects.filter(id__in=RawSQL('SELECT g.id FROM api_event e, api_user u,api_group g, \
    # api_user_group ug, api_agent a \
    # where a.user_id=u.id and e.agent_id=a.id and e.level="information" \
    # and u.id=ug.user_id and g.id=ug.group_id', params=()))
    # queryset = Group.objects.annotate(id=FilteredRelation(
    #     'api_agent', condition=Q(api_agent__level='information'),),).filter()
    # event_information = Event.objects.filter(level='information')
    # agent_information = Agent.objects.filter(event__level='information')
    # user_information = User.objects.filter(agent__event__level='informantion')
    group_information = Group.objects.filter(
        user__agent__event__level='information')
    # queryset = Group.objects.filter(user_id=agenda__user_id)
    return group_information
