
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
import django
django.setup()
from main import (
    get_active_users,
    get_amount_users,
    get_admin_users,
    get_all_debug_events,
    get_all_critical_events_by_user,
    get_all_agents_by_user,
    get_all_events_by_group
)
from datetime import datetime, timedelta
from api.models import User, Agent, Event, Group



Event.objects.all().delete()
Agent.objects.all().delete()
User.objects.all().delete()
Group.objects.all().delete()