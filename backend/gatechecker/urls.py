from django.conf.urls import url, include
from django.urls import path
from . import views
from . import documents


urlpatterns = [
    # 下面是类视图名
    path('', views.IndexView.as_view(), name='index'),
    url(r'apis', views.apis, name='apis'),

    url(r'get_users$', views.get_users, name='get_users'),
    url(r'get_users_id', views.get_users_id, name='get_users_id'),
    url(r'add_user', views.add_user, name='add_user'),
    url(r'update_user', views.update_user, name='update_user'),
    url(r'remove_user', views.remove_user, name='remove_user'),

    url(r'get_buildings$', views.get_buildings, name='get_buildings'),
    url(r'get_buildings_id', views.get_buildings_id, name='get_buildings_id'),
    url(r'add_building', views.add_building, name='add_building'),
    url(r'update_building', views.update_building, name='update_building'),
    url(r'remove_building', views.remove_building, name='remove_building'),

    url(r'get_gates$', views.get_gates, name='get_gates'),
    url(r'get_gates_id', views.get_gates_id, name='get_gates_id'),
    url(r'add_gate', views.add_gate, name='add_gate'),
    url(r'update_gate', views.update_gate, name='update_gate'),
    url(r'remove_gate', views.remove_gate, name='remove_gate'),

    url(r'get_devices$', views.get_devices, name='get_devices'),
    url(r'get_devices_id', views.get_devices_id, name='get_devices_id'),
    url(r'add_device', views.add_device, name='add_device'),
    url(r'update_device', views.update_device, name='update_device'),
    url(r'remove_device', views.remove_device, name='remove_device'),

    url(r'get_logs', views.get_logs, name='get_logs'),
    url(r'add_log', views.add_log, name='add_log'),
    url(r'update_log', views.update_log, name='update_log'),
    url(r'remove_log', views.remove_log, name='remove_log'),

    url(r'get_count$', views.get_count, name='get_count'),
    url(r'get_count_single', views.get_count_single, name='get_count_single'),
    url(r'get_alarm', views.get_alarm, name='get_alarm'),
    url(r'clear_alarm_by_building_name', views.clear_alarm_by_building_name, name='clear_alarm_by_building_name'),

    url(r'report', documents.report, name='report'),
]
