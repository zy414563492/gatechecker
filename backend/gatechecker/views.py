from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views import generic
import json
from .models import User, Building, Gate, Device, Log
from django.core import serializers
from datetime import datetime


class IndexView(generic.View):
    def get(self, request):
        # get请求
        return HttpResponse('这是get请求')

    def post(self, request):
        # post请求
        return HttpResponse('这是post请求')

    def put(self, request):
        # 其他请求
        return HttpResponse('这是其他请求')


def apis(request):
    print("hello input")
    # p={"word":"data"}
    # 查看客户端发来的请求,前端的数据
    print("request.body={}".format(request.body))
    # 返回给客户端的数据
    result = "success"
    if request.method == "POST":
        print(request.POST)

    user_input = json.loads(str(request.body, 'utf-8'))

    # print(user_input['a'])

    output = int(user_input['a']) + int(user_input['b'])

    return JsonResponse({"status": 200, "msg": "OK", "data": output})


def to_bool(x):
    return x in ("True", "true", True)


# ***************************************************************************** #
#                                ---> Admin <---                                #
# ***************************************************************************** #


# ***************************************************************************** #
#                                ---> Users <---                                #
# ***************************************************************************** #

# POST: http://localhost:8000/gatechecker/get_users_id
def get_users_id(request):
    user_query = User.objects.all()
    users_id = [u.user_id for u in user_query]
    return HttpResponse(json.dumps({"users": users_id}), content_type="application/json")


# POST: http://localhost:8000/gatechecker/get_users
def get_users(request):
    user_dic = {'user_list': []}
    user_query = User.objects.all()
    for user in user_query:
        _dic = user.obj_to_dic()

        # 本エンドユーザーの施設を表示する
        with_buildings_query = user.building_set.all()
        with_buildings = [b.building_id for b in with_buildings_query]
        _dic['with_buildings'] = with_buildings
        print(_dic)

        user_dic['user_list'].append(_dic)

    return HttpResponse(json.dumps(user_dic), content_type="application/json")


# POST: http://localhost:8000/gatechecker/add_user
# JSON例:
# {
#     "user_id": "U1",
#     "name": "三井不動産",
# }
def add_user(request):
    # frontendからのデータを表示する
    print("request.body={}".format(request.body))

    user_input = json.loads(str(request.body, 'utf-8'))
    user_id = user_input['user_id']
    name = user_input['name']

    user = User(user_id=user_id, name=name)

    # データベースに書く
    user.save()
    print("書き込み成功\n")

    return HttpResponse(json.dumps(user.obj_to_dic()), content_type="application/json")


# POST: http://localhost:8000/gatechecker/update_user
# JSON例:
# {
#     "user_id": "U1",
#     "name": "Yahoo不動産",
# }
def update_user(request):
    # frontendからのデータを表示する
    print("request.body={}".format(request.body))

    user_input = json.loads(str(request.body, 'utf-8'))
    user_id = user_input['user_id']
    name = user_input['name']

    user = User.objects.get(user_id=user_id)
    user.name = name

    print("user:\n", user)

    # データベースに書く
    user.save()
    print("書き込み成功\n")

    return HttpResponse(json.dumps(user.obj_to_dic()), content_type="application/json")


# POST: http://localhost:8000/gatechecker/remove_user
# JSON例:
# {
#     "user_id": "U2"
# }
def remove_user(request):
    # frontendからのデータを表示する
    print("request.body={}".format(request.body))

    user_id = json.loads(str(request.body, 'utf-8'))["user_id"]
    user = User.objects.get(user_id=user_id)
    print("user:\n", user)

    res = user.obj_to_dic()

    # データベースから削除する
    user.delete()
    print("削除成功\n")

    return HttpResponse(json.dumps(res), content_type="application/json")


# ***************************************************************************** #
#                              ---> Buildings <---                              #
# ***************************************************************************** #


# POST: http://localhost:8000/gatechecker/get_buildings_id
def get_buildings_id(request):
    building_query = Building.objects.all()
    buildings_id = [b.building_id for b in building_query]
    return HttpResponse(json.dumps({"buildings": buildings_id}), content_type="application/json")


# POST: http://localhost:8000/gatechecker/get_buildings
def get_buildings(request):
    building_dic = {'building_list': []}
    building_query = Building.objects.all()
    for building in building_query:
        _dic = building.obj_to_dic()

        # 本施設の所有者
        _dic['to_user'] = str(building.to_user)     # User Object -> str

        # 本施設のゲートを表示する
        with_gates_query = building.gate_set.all()
        with_gates = [g.gate_id for g in with_gates_query]
        _dic['with_gates'] = with_gates
        print(_dic)

        building_dic['building_list'].append(_dic)

    return HttpResponse(json.dumps(building_dic), content_type="application/json")


# POST: http://localhost:8000/gatechecker/add_building
# JSON例:
# {
#     "building_id": "B1",
#     "name": "sky tree",
#     "location": "Tokyo",
#     "to_user": "U1"
# }
def add_building(request):
    # frontendからのデータを表示する
    print("request.body={}".format(request.body))

    building_input = json.loads(str(request.body, 'utf-8'))
    building_id = building_input['building_id']
    name = building_input['name']
    location = building_input['location']
    to_user = building_input['to_user']

    if User.objects.filter(user_id=to_user).exists():
        user = User.objects.get(user_id=to_user)
        building = Building(building_id=building_id, name=name, location=location, to_user=user)
    else:
        building = Building(building_id=building_id, name=name, location=location)

    # データベースに書く
    building.save()
    print("書き込み成功\n")

    return HttpResponse(json.dumps(building.obj_to_dic()), content_type="application/json")


# POST: http://localhost:8000/gatechecker/update_building
# JSON例:
# {
#     "building_id": "B1",
#     "name": "sky tree hotel",
#     "location": "Tokyo",
#     "to_user": "U1"
# }
def update_building(request):
    # frontendからのデータを表示する
    print("request.body={}".format(request.body))

    building_input = json.loads(str(request.body, 'utf-8'))
    building_id = building_input['building_id']
    name = building_input['name']
    location = building_input['location']
    to_user = building_input['to_user']

    user = User.objects.get(user_id=to_user)

    building = Building.objects.get(building_id=building_id)
    building.name = name
    building.location = location
    building.to_user = user

    print("building:\n", building)

    # データベースに書く
    building.save()
    print("書き込み成功\n")

    return HttpResponse(json.dumps(building.obj_to_dic()), content_type="application/json")


# POST: http://localhost:8000/gatechecker/remove_building
# JSON例:
# {
#     "building_id": "B2"
# }
def remove_building(request):
    # frontendからのデータを表示する
    print("request.body={}".format(request.body))

    building_id = json.loads(str(request.body, 'utf-8'))["building_id"]
    building = Building.objects.get(building_id=building_id)
    print("building:\n", building)

    res = building.obj_to_dic()

    # データベースから削除する
    building.delete()
    print("削除成功\n")

    return HttpResponse(json.dumps(res), content_type="application/json")


# ***************************************************************************** #
#                                ---> Gates <---                                #
# ***************************************************************************** #


# POST: http://localhost:8000/gatechecker/get_gates_id
def get_gates_id(request):
    gate_query = Gate.objects.all()
    gates_id = [g.gate_id for g in gate_query]
    return HttpResponse(json.dumps({"gates": gates_id}), content_type="application/json")


# POST: http://localhost:8000/gatechecker/get_gates
def get_gates(request):
    gate_dic = {'gate_list': []}
    gate_query = Gate.objects.all()
    for gate in gate_query:
        _dic = gate.obj_to_dic()

        # 本ゲートの所属施設
        _dic['to_building'] = str(gate.to_building)  # Gate Object -> str

        # 本ゲートのデバイスを表示する
        with_devices_query = gate.device_set.all()
        with_devices = [d.device_id for d in with_devices_query]
        _dic['with_devices'] = with_devices
        print(_dic)

        gate_dic['gate_list'].append(_dic)

    return HttpResponse(json.dumps(gate_dic), content_type="application/json")


# POST: http://localhost:8000/gatechecker/add_gate
# JSON例:
# {
#     "gate_id": "G1",
#     "name": "南正門",
#     "is_open": true
# }
def add_gate(request):
    # frontendからのデータを表示する
    print("request.body={}".format(request.body))

    gate_input = json.loads(str(request.body, 'utf-8'))
    gate_id = gate_input['gate_id']
    name = gate_input['name']
    is_open = to_bool(gate_input['is_open'])
    to_building = gate_input['to_building']

    print("gate_id: {}\nname: {}\nis_open: {}\nto_building: {}\n".format(gate_id, name, str(is_open), to_building))

    if Building.objects.filter(building_id=to_building).exists():
        building = Building.objects.get(building_id=to_building)
        gate = Gate(gate_id=gate_id, name=name, is_open=is_open, to_building=building)
    else:
        gate = Gate(gate_id=gate_id, name=name, is_open=is_open)

    # データベースに書く
    gate.save()
    print("書き込み成功\n")

    return HttpResponse(json.dumps(gate.obj_to_dic()), content_type="application/json")


# POST: http://localhost:8000/gatechecker/update_gate
# JSON例:
# {
#     "gate_id": "G1",
#     "name": "南正門",
#     "is_open": false
# }
def update_gate(request):
    # frontendからのデータを表示する
    print("request.body={}".format(request.body))

    gate_input = json.loads(str(request.body, 'utf-8'))
    gate_id = gate_input['gate_id']
    name = gate_input['name']
    is_open = gate_input['is_open']
    to_building = gate_input['to_building']

    building = Building.objects.get(building_id=to_building)

    gate = Gate.objects.get(gate_id=gate_id)
    gate.name = name
    gate.is_open = is_open
    gate.to_building = building

    print("gate:\n", gate)

    # データベースに書く
    gate.save()
    print("書き込み成功\n")

    return HttpResponse(json.dumps(gate.obj_to_dic()), content_type="application/json")


# POST: http://localhost:8000/gatechecker/remove_gate
# JSON例:
# {
#     "gate_id": "G1"
# }
def remove_gate(request):
    # frontendからのデータを表示する
    print("request.body={}".format(request.body))

    gate_id = json.loads(str(request.body, 'utf-8'))["gate_id"]
    gate = Gate.objects.get(gate_id=gate_id)
    print("gate:\n", gate)

    res = gate.obj_to_dic()

    # データベースから削除する
    gate.delete()
    print("削除成功\n")

    return HttpResponse(json.dumps(res), content_type="application/json")


# ***************************************************************************** #
#                               ---> Devices <---                               #
# ***************************************************************************** #

# POST: http://localhost:8000/gatechecker/get_devices_id
def get_devices_id(request):
    device_query = Device.objects.all()
    devices_id = [d.device_id for d in device_query]
    return HttpResponse(json.dumps({"devices": devices_id}), content_type="application/json")


# POST: http://localhost:8000/gatechecker/get_devices
def get_devices(request):
    device_dic = {'device_list': []}
    device_query = Device.objects.all()
    for device in device_query:
        _dic = device.obj_to_dic()

        # 本デバイスの所属ゲート
        _dic['to_gate'] = str(device.to_gate)  # Device Object -> str

        # 本デバイスのログを表示する
        with_logs_query = device.log_set.all()
        with_logs = [log.log_id for log in with_logs_query]
        _dic['with_logs'] = with_logs
        print(_dic)

        device_dic['device_list'].append(_dic)

    return HttpResponse(json.dumps(device_dic), content_type="application/json")


# POST: http://localhost:8000/gatechecker/add_device
# JSON例:
# {
#     "device_id": "D1",
#     "is_entrance": true,
#     "is_using": true,
#     "last_alert_time": "2020-10-10 10:10:10",
#     "to_gate": "G1"
# }
def add_device(request):
    # frontendからのデータを表示する
    print("request.body={}".format(request.body))

    device_input = json.loads(str(request.body, 'utf-8'))
    device_id = device_input['device_id']
    is_entrance = to_bool(device_input['is_entrance'])
    is_using = to_bool(device_input['is_using'])
    last_alert_time = datetime.strptime(device_input['last_alert_time'], '%Y-%m-%d %H:%M:%S')
    to_gate = device_input['to_gate']

    print("device_id: {}\nis_entrance: {}\nis_using: {}\nlast_alert_time: {}\nto_building: {}\n"
          .format(device_id, str(is_entrance), str(is_using), str(last_alert_time), to_gate))

    if Gate.objects.filter(gate_id=to_gate).exists():
        gate = Gate.objects.get(gate_id=to_gate)
        device = Device(device_id=device_id, is_entrance=is_entrance, is_using=is_using, last_alert_time=last_alert_time,
                        to_gate=gate)
    else:
        device = Device(device_id=device_id, is_entrance=is_entrance, is_using=is_using, last_alert_time=last_alert_time)

    # データベースに書く
    device.save()
    print("書き込み成功\n")

    return HttpResponse(json.dumps(device.obj_to_dic()), content_type="application/json")


# POST: http://localhost:8000/gatechecker/update_device
# JSON例:
# {
#     "device_id": "D1",
#     "is_entrance": true,
#     "is_using": true,
#     "last_alert_time": "2020-10-10 10:10:10",
#     "to_gate": "G1"
# }
def update_device(request):
    # frontendからのデータを表示する
    print("request.body={}".format(request.body))

    device_input = json.loads(str(request.body, 'utf-8'))
    device_id = device_input['device_id']
    is_entrance = device_input['is_entrance']
    is_using = device_input['is_using']
    last_alert_time = datetime.strptime(device_input['last_alert_time'], '%Y-%m-%d %H:%M:%S')
    to_gate = device_input['to_gate']

    gate = Gate.objects.get(gate_id=to_gate)

    device = Device.objects.get(device_id=device_id)
    device.is_entrance = is_entrance
    device.is_using = is_using
    device.last_alert_time = last_alert_time
    device.to_gate = gate

    # データベースに書く
    device.save()
    print("書き込み成功\n")

    return HttpResponse(json.dumps(device.obj_to_dic()), content_type="application/json")


# POST: http://localhost:8000/gatechecker/remove_device
# JSON例:
# {
#     "device_id": "D1"
# }
def remove_device(request):
    # frontendからのデータを表示する
    print("request.body={}".format(request.body))

    device_id = json.loads(str(request.body, 'utf-8'))["device_id"]
    device = Device.objects.get(device_id=device_id)
    print("device:\n", device)

    res = device.obj_to_dic()

    # データベースから削除する
    device.delete()
    print("削除成功\n")

    return HttpResponse(json.dumps(res), content_type="application/json")


# ***************************************************************************** #
#                                ---> Logs <---                                 #
# ***************************************************************************** #


# POST: http://localhost:8000/gatechecker/get_logs
def get_logs(request):
    log_dic = {'log_list': []}
    log_query = Log.objects.all()

    for log in log_query:
        _dic = log.obj_to_dic()

        # 本記録を持っているデバイス
        _dic['to_device'] = str(log.to_device)  # Log Object -> str

        log_dic['log_list'].append(_dic)
        print(_dic)

    return HttpResponse(json.dumps(log_dic), content_type="application/json")


# POST: http://localhost:8000/gatechecker/add_device
# JSON例:
# {
#     "log_id": "L001",
#     "temperature": 35.8,
#     "time": "2021-09-01 19:34:10",
#     "is_blacklist": true,
#     "to_device": "D1"
# }
def add_log(request):
    # frontendからのデータを表示する
    print("request.body={}".format(request.body))

    log_input = json.loads(str(request.body, 'utf-8'))
    log_id = log_input['log_id']
    temperature = float(log_input['temperature'])
    time = datetime.strptime(log_input['time'], '%Y-%m-%d %H:%M:%S')
    is_blacklist = to_bool(log_input['is_blacklist'])
    to_device = log_input['to_device']

    print("log_id: {}\ntemperature: {}\ntime: {}\nis_blacklist: {}\nto_device: {}\n"
          .format(log_id, str(temperature), str(time), str(is_blacklist), to_device))

    device = Device.objects.get(device_id=to_device)

    log = Log(log_id=log_id, temperature=temperature, time=time, is_blacklist=is_blacklist,
              to_device=device)

    # データベースに書く
    log.save()
    print("書き込み成功\n")

    return HttpResponse(json.dumps(log.obj_to_dic()), content_type="application/json")


# POST: http://localhost:8000/gatechecker/update_log
# JSON例:
# {
#     "log_id": "L001",
#     "temperature": 36.8,
#     "time": "2021-09-01 19:34:10",
#     "is_blacklist": true,
#     "to_device": "D1"
# }
def update_log(request):
    # frontendからのデータを表示する
    print("request.body={}".format(request.body))

    log_input = json.loads(str(request.body, 'utf-8'))
    log_id = log_input['log_id']
    temperature = log_input['temperature']
    time = datetime.strptime(log_input['time'], '%Y-%m-%d %H:%M:%S')
    is_blacklist = log_input['is_blacklist']
    to_device = log_input['to_device']

    device = Device.objects.get(device_id=to_device)

    log = Log.objects.get(log_id=log_id)
    log.temperature = temperature
    log.time = time
    log.is_blacklist = is_blacklist
    log.to_device = device

    # データベースに書く
    log.save()
    print("書き込み成功\n")

    return HttpResponse(json.dumps(log.obj_to_dic()), content_type="application/json")


# POST: http://localhost:8000/gatechecker/remove_log
# JSON例:
# {
#     "log_id": "L001"
# }
def remove_log(request):
    # frontendからのデータを表示する
    print("request.body={}".format(request.body))

    log_id = json.loads(str(request.body, 'utf-8'))["log_id"]
    log = Log.objects.get(log_id=log_id)
    print("log:\n", log)

    res = log.obj_to_dic()

    # データベースから削除する
    log.delete()
    print("削除成功\n")

    return HttpResponse(json.dumps(res), content_type="application/json")


# ***************************************************************************** #
#                               ---> Results <---                               #
# ***************************************************************************** #


# POST: http://localhost:8000/gatechecker/get_count
def get_count(request):
    count_dic = {'count_info': []}
    building_query = Building.objects.all()
    for building in building_query:
        _dic = dict()
        _dic['name'] = building.name
        _dic['to_user'] = str(building.to_user)
        _dic['count_enter'] = building.count_enter()
        _dic['count_exit'] = building.count_exit()
        _dic['count_inside'] = building.count_inside()
        _dic['has_blacklist'] = len(building.get_alert_state()['building_name']) > 0
        count_dic['count_info'].append(_dic)
        print(_dic)
    return HttpResponse(json.dumps(count_dic), content_type="application/json")


# POST: http://localhost:8000/gatechecker/get_alarm
def get_alarm(request):
    alarm_dic = {'alarm_info': []}
    building_query = Building.objects.all()
    for building in building_query:
        print("building: ", building)
        _dic = building.get_alert_state()
        print(_dic)
        print(len(_dic['building_name']) > 0)
        alarm_dic['alarm_info'].append(_dic)
    return HttpResponse(json.dumps(alarm_dic), content_type="application/json")


# POST: http://localhost:8000/gatechecker/clear_alarm_by_building_name
def clear_alarm_by_building_name(request):
    # frontendからのデータを表示する
    print("request.body={}".format(request.body))

    input = json.loads(str(request.body, 'utf-8'))
    building_name = input['building_name']
    building = Building.objects.get(name=building_name)

    print("building:", building.obj_to_dic())
    building.clear_alarm()

    return HttpResponse(json.dumps(building.obj_to_dic()), content_type="application/json")




