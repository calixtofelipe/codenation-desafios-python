from django.shortcuts import render
from datetime import datetime, timedelta,date

from api.models import User, Agent, Event, Group

def get_active_users(self):
    dt = datetime.now()
    d_truncated = date(dt.year, dt.month, dt.day)
    date_filter = d_truncated-timedelta(days=10)
    queryset = User.objects.raw('SELECT * FROM api_user u \
    where u.last_login >=%s  order by u.name', [date_filter])
    return queryset


def get_amount_users() -> User:
    queryset = User.objects.raw('SELECT 1 as id, COUNT(*) as qtduser FROM api_user u')
    return queryset.qtduser


def get_admin_users() -> User:
    """Traga todos os usuarios com grupo = 'admin"""
    queryset = User.objects.raw('SELECT * FROM api_user u, \
         api_user_group ug, api_group g where u.id=ug.user_id and  \
         ug.group_id=g.id and g.name = "admin" order by u.name')
    return queryset


def get_all_debug_events() -> Event:
    """Traga todos os eventos com tipo debug"""
    def get_all_debug_events(self):
        queryset = Event.objects.raw('SELECT * FROM api_event where level= "debug" ')
        return queryset


def get_all_critical_events_by_user(agent) -> Event:
    """Traga todos os eventos do tipo critico de um usuário específico"""
    raise NotImplementedError


def get_all_agents_by_user(username) -> Agent:
    """Traga todos os agentes de associados a um usuário pelo nome do usuário"""
    def get_all_agents_by_user(self, username):
        queryset = Agent.objects.raw('SELECT * FROM api_user u, api_agent a \
            where a.user_id=u.id and u.name=%s', [username])
        return queryset


def get_all_events_by_group() -> Group:
    """Traga todos os grupos que contenham alguem que possua um agente que possuem eventos do tipo information"""
    def get_all_events_by_group(self):
        queryset = Event.objects.raw('SELECT g.* FROM api_event e, api_user u,api_group g, \
        api_user_group ug, api_agent a \
        where a.user_id=u.id and e.agent_id=a.id and e.level="information" \
        and u.id=ug.user_id and g.id=ug.group_id')
        return queryset

