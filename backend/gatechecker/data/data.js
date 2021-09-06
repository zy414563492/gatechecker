// Example POST JSONs


// Add Users
{
    "user_id": "U1",
    "name": "三井不動産"
}
{
    "user_id": "U2",
    "name": "Yahoo不動産"
}
{
    "user_id": "U3",
    "name": "北海道不動産"
}

{
    "user_id": "U4",
    "name": "東横イン"
}

{
    "user_id": "U5",
    "name": "野村不動産"
}
{
    "user_id": "U6",
    "name": "セキスイハイム"
}
{
    "user_id": "U7",
    "name": "飯田ホールディングス"
}
{
    "user_id": "U8",
    "name": "住友林業"
}
{
    "user_id": "U9",
    "name": "ヘーベルハウス"
}


// Add Buildings
{
    "building_id": "B1",
    "name": "sky tree",
    "location": "Tokyo",
    "to_user": "U1"
}
{
    "building_id": "B2",
    "name": "iias",
    "location": "Tsukuba",
    "to_user": "U1"
}
{
    "building_id": "B3",
    "name": "AEON Mall",
    "location": "Tsuchiura",
    "to_user": "U2"
}
{
    "building_id": "B4",
    "name": "Wing",
    "location": "Hitachinaka",
    "to_user": "U2"
}
{
    "building_id": "B5",
    "name": "Cross Hotel",
    "location": "Sapporo",
    "to_user": "U3"
}


// Add Gates
{
    "gate_id": "G1",
    "name": "正門",
    "is_open": true,
    "to_building": "B1"
}
{
    "gate_id": "G2",
    "name": "東門",
    "is_open": false,
    "to_building": "B2"
}
{
    "gate_id": "G3",
    "name": "西門",
    "is_open": true,
    "to_building": "B2"
}
{
    "gate_id": "G4",
    "name": "南門",
    "is_open": true,
    "to_building": "B2"
}
{
    "gate_id": "G5",
    "name": "正門",
    "is_open": true,
    "to_building": "B3"
}
{
    "gate_id": "G6",
    "name": "正門",
    "is_open": true,
    "to_building": "B4"
}
{
    "gate_id": "G7",
    "name": "正門",
    "is_open": true,
    "to_building": "B5"
}


// Add Devices
{
    "device_id": "D1",
    "is_entrance": true,
    "is_using": true,
    "last_alert_time": "2020-10-10 10:10:10",
    "to_gate": "G1"
}
{
    "device_id": "D2",
    "is_entrance": false,
    "is_using": true,
    "last_alert_time": "2020-10-10 10:10:10",
    "to_gate": "G1"
}
{
    "device_id": "D3",
    "is_entrance": true,
    "is_using": true,
    "last_alert_time": "2020-10-10 10:10:10",
    "to_gate": "G3"
}
{
    "device_id": "D4",
    "is_entrance": false,
    "is_using": true,
    "last_alert_time": "2020-10-10 10:10:10",
    "to_gate": "G4"
}


// Add Logs
{
    "log_id": "L001",
    "temperature": 35.8,
    "time": "2021-09-01 19:34:10",
    "is_blacklist": true,
    "to_device": "D1"
}
{
    "log_id": "L002",
    "temperature": 36.4,
    "time": "2021-09-01 19:36:23",
    "is_blacklist": false,
    "to_device": "D1"
}
{
    "log_id": "L003",
    "temperature": 35.7,
    "time": "2021-09-01 19:48:23",
    "is_blacklist": true,
    "to_device": "D2"
}
{
    "log_id": "L004",
    "temperature": 36.3,
    "time": "2021-09-01 19:51:47",
    "is_blacklist": false,
    "to_device": "D2"
}