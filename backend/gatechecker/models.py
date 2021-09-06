from django.db import models
from datetime import datetime


# エンドユーザークラス
class User(models.Model):
    user_id = models.CharField(max_length=20, primary_key=True)
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.user_id
        # return "user_id: {}\nname: {}\n".format(self.user_id, self.name)

    def obj_to_dic(self):
        return {"user_id": self.user_id, "name": self.name}


# 施設クラス
class Building(models.Model):
    building_id = models.CharField(max_length=20, primary_key=True)
    name = models.CharField(max_length=20)
    location = models.TextField(max_length=100)
    to_user = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )

    def __str__(self):
        return self.building_id
        # return "building_id: {}\nname: {}\nlocation: {}\n".format(self.building_id, self.name, self.location)

    def obj_to_dic(self):
        return {"building_id": self.building_id, "name": self.name, "location": self.location}

    # 累計入場者数（=当施設入口用デバイス検温総回数） [int][人]
    def count_enter(self) -> int:
        return sum([g.count_enter() for g in self.gate_set.all()])

    # 累計退場者数（=当施設出口用デバイス検温総回数） [int][人]
    def count_exit(self) -> int:
        return sum([g.count_exit() for g in self.gate_set.all()])

    # 今施設内にいる人数 [int][人]
    def count_inside(self) -> int:
        return self.count_enter() - self.count_exit()

    # 施設状態の更新
    def get_alert_state(self):
        # alert_dict = {"building_name": "", "gate_name": "", "sensor_id": "", "time": ""}
        alert_dict = {"building_name": [], "gate_name": [], "sensor_id": [], "time": []}
        for idx, gate in enumerate(self.gate_set.all()):
            gate_dict = gate.get_alert_state()
            if gate_dict['gate_name'] is not []:
                # print("ALARM! 施設: {}, ゲート: {}, デバイス: {}, 時間: {}\nブラックリストを検知した"
                #       .format(self.name, gate_dict['gate_name'], gate_dict['sensor_id'], gate_dict['time']))
                # alert_dict['building_name'] = self.name
                # alert_dict['gate_name'] = gate_dict['gate_name']
                # alert_dict['sensor_id'] = gate_dict['sensor_id']
                # alert_dict['time'] = gate_dict['time']
                for i in range(len(gate_dict['sensor_id'])):
                    alert_dict['building_name'].append(self.name)
                    alert_dict['gate_name'].append(gate_dict['gate_name'][i])
                    alert_dict['sensor_id'].append(gate_dict['sensor_id'][i])
                    alert_dict['time'].append(gate_dict['time'][i])
        return alert_dict

    # 手動で施設のアラームを解除する
    def clear_alarm(self):
        for idx, gate in enumerate(self.gate_set.all()):
            gate.clear_alarm()


# 出入口クラス
class Gate(models.Model):
    gate_id = models.CharField(max_length=20, primary_key=True)
    name = models.CharField(max_length=20)
    is_open = models.BooleanField(default=True)
    to_building = models.ForeignKey(
        Building,
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )

    def __str__(self):
        return self.gate_id
        # return "gate_id: {}\nname: {}\nis_open: {}\n".format(self.gate_id, self.name, str(self.is_open))

    def obj_to_dic(self):
        return {"gate_id": self.gate_id, "name": self.name, "is_open": self.is_open}

    # 入場者数（=当ゲート入口専用デバイスの検温回数） [int][人]
    def count_enter(self) -> int:
        return sum([d.count() for d in self.device_set.all() if self.is_open and d.is_using and d.is_entrance])

    # 退場者数（=当ゲート出口専用デバイスの検温回数） [int][人]
    def count_exit(self) -> int:
        return sum([d.count() for d in self.device_set.all() if self.is_open and d.is_using and d.is_entrance is False])

    # 当ゲートの純流入人数 [int][人]
    def count_inflow(self) -> int:
        return self.count_enter() - self.count_exit()

    # ゲート状態の更新
    def get_alert_state(self):
        # alert_dict = {"gate_name": "", "sensor_id": "", "time": ""}
        alert_dict = {"gate_name": [], "sensor_id": [], "time": []}
        for idx, device in enumerate(self.device_set.all()):
            device_dict = device.get_alert_state()
            if device_dict['sensor_id'] is not []:
                # print("ALARM! ゲート: {}, デバイス: {}, 時間: {}\nブラックリストを検知した"
                #       .format(self.name, device_dict['sensor_id'], device_dict['time']))
                # alert_dict['gate_name'] = self.name
                # alert_dict['sensor_id'] = device_dict['sensor_id']
                # alert_dict['time'] = device_dict['time']
                for i in range(len(device_dict['sensor_id'])):
                    alert_dict['gate_name'].append(self.name)
                    alert_dict['sensor_id'].append(device_dict['sensor_id'][i])
                    alert_dict['time'].append(device_dict['time'][i])
        return alert_dict

    # 手動でゲートのアラームを解除する
    def clear_alarm(self):
        for idx, device in enumerate(self.device_set.all()):
            device.clear_alarm()


# デバイスクラス
class Device(models.Model):
    device_id = models.CharField(max_length=20, primary_key=True)
    is_entrance = models.BooleanField(default=True)
    is_using = models.BooleanField(default=True)
    last_alert_time = models.DateTimeField(auto_now=False)
    to_gate = models.ForeignKey(
        Gate,
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )

    def __str__(self):
        return self.device_id

    def obj_to_dic(self) -> dict:
        return {"device_id": self.device_id, "is_entrance": self.is_entrance,
                "is_using": self.is_using, "last_alert_time": str(self.last_alert_time)}

    def count(self):
        return len(self.log_set.all())

    # デバイス状態の更新
    # ブラックリストに該当する記録があればいつでもアラートしてしまうというエラーを避けるため、
    # 前回アラートの時点以後の記録のみ検査をする
    def get_alert_state(self):
        # alert_dict = {"sensor_id": "", "time": ""}
        alert_dict = {"sensor_id": [], "time": []}
        for idx, log in enumerate(self.log_set.all()):
            if log.is_blacklist and log.time > self.last_alert_time:
                # print("ALARM! 時間：{}\nブラックリストを検知した".format(str(log.time)))
                # alert_dict['sensor_id'] = self.sensor_id
                # alert_dict['time'] = str(log.time)
                alert_dict['sensor_id'].append(self.device_id)
                alert_dict['time'].append(str(log.time))
        return alert_dict

    # 手動でデバイスのアラームを解除する
    def clear_alarm(self):
        self.last_alert_time = datetime.now()
        self.save()
        print("書き込み成功\n")


# 検温記録クラス
class Log(models.Model):
    log_id = models.CharField(max_length=20, primary_key=True)
    temperature = models.FloatField()
    time = models.DateTimeField(auto_now=False)
    is_blacklist = models.BooleanField(default=True)
    to_device = models.ForeignKey(
        Device,
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )

    def __str__(self):
        return self.log_id

    def obj_to_dic(self):
        return {"log_id": self.log_id, "temperature": self.temperature,
                "time": str(self.time), "is_blacklist": self.is_blacklist}









