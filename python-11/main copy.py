from api.models import User, Agent, Event, Group
from datetime import datetime, timedelta
from django.db.models.expressions import RawSQL

def get_active_users():
    dt = datetime.now()
    d_truncated = datetime.date(dt.year, dt.month, dt.day)
    date_filter = d_truncated-datetime.timedelta(days=10)
    rqueryset = User.objects.raw('SELECT * FROM api_user u \
    where u.last_login >=%s  order by u.name', [date_filter])
    queryset = User.objects.filter(id__in=RawSQL('SELECT u.id FROM api_user u \
    where u.last_login >=%s  order by u.name', [date_filter]))
    return queryset


def get_amount_users() -> User:
    rqueryset = User.objects.raw('SELECT 1 as id, COUNT(*) as qtduser FROM api_user u')
    queryset = User.objects.filter(id__in=RawSQL('SELECT u.id FROM api_user u',params=()))
    return User.objects.count()


def get_admin_users() -> User:
    """Traga todos os usuarios com grupo = 'admin"""
    rqueryset = User.objects.raw('SELECT * FROM api_user u, \
         api_user_group ug, api_group g where u.id=ug.user_id and  \
         ug.group_id=g.id and g.name = "admin" order by u.name')
    queryset = User.objects.filter(id__in=RawSQL('SELECT u.id FROM api_user u, \
         api_user_group ug, api_group g where u.id=ug.user_id and  \
         ug.group_id=g.id and g.name = "admin" order by u.name',params=()))
    return queryset


def get_all_debug_events() -> Event:
    """Traga todos os eventos com tipo debug"""
    rqueryset = Event.objects.raw('SELECT * FROM api_event where level= "debug" ')
    queryset = Event.objects.filter(id__in=RawSQL('SELECT e.id FROM api_event e where e.level= "debug" ',params=()))
    return queryset


def get_all_critical_events_by_user(agent) -> Event:
    """Traga todos os eventos do tipo critico de um agente específico"""
    rqueryset = Event.objects.raw('SELECT e.* FROM api_event e, api_user u, api_agent a \
            where a.user_id=u.id and e.agent_id=a.id and e.level="critical" and a.id=%s', [agent.id])
    queryset = Event.objects.filter(id__in=RawSQL('SELECT e.id FROM api_event e, api_user u, api_agent a \
            where a.user_id=u.id and e.agent_id=a.id and e.level="critical" and a.id=%s', [agent.id]))
    return queryset


def get_all_agents_by_user(username) -> Agent:
    """Traga todos os agentes de associados a um usuário pelo nome do usuário"""
    rqueryset = Agent.objects.raw('SELECT * FROM api_user u, api_agent a \
            where a.user_id=u.id and u.name=%s', [username])
    queryset = Agent.objects.filter(id__in=RawSQL('SELECT a.id FROM api_user u, api_agent a \
            where a.user_id=u.id and u.name=%s', [username]))
    return queryset


def get_all_events_by_group() -> Group:
    """Traga todos os grupos que contenham alguem que possua um agente que possuem eventos do tipo information"""
    rqueryset = Group.objects.raw('SELECT g.* FROM api_event e, api_user u,api_group g, \
    api_user_group ug, api_agent a \
    where a.user_id=u.id and e.agent_id=a.id and e.level="information" \
    and u.id=ug.user_id and g.id=ug.group_id')
    queryset = Group.objects.filter(id__in=RawSQL('SELECT g.id FROM api_event e, api_user u,api_group g, \
    api_user_group ug, api_agent a \
    where a.user_id=u.id and e.agent_id=a.id and e.level="information" \
    and u.id=ug.user_id and g.id=ug.group_id',params=()))
    return queryset
