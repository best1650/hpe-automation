from flask import Flask, render_template, request, jsonify, redirect, url_for

app = Flask(__name__)

# Mock Data
system_info = {
    "Id": "1",
    "Name": "HPE ProLiant DL380 Gen10",
    "SystemType": "Physical",
    "AssetTag": "Mock-Asset-123",
    "Manufacturer": "HPE",
    "Model": "ProLiant DL380 Gen10",
    "SerialNumber": "SGH1234567",
    "Status": {
        "State": "Enabled",
        "Health": "OK"
    },
    "PowerState": "On",
    "BiosVersion": "U30 v2.42 (04/16/2021)"
}

power_info_data = {
    "PowerConsumedWatts": 250,
    "PowerCapacityWatts": 800
}

manager_info_data = {
    "Name": "iLO 5",
    "FirmwareVersion": "2.42"
}

@app.route('/')
def login():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def do_login():
    username = request.form.get('username')
    password = request.form.get('password')
    # Simple mock check
    if username == "admin" and password == "password":
        return redirect(url_for('dashboard'))
    return redirect(url_for('login', error="Invalid credentials"))

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html', system=system_info, power=power_info_data, manager=manager_info_data)

# Redfish API
@app.route('/redfish/v1/')
def redfish_root():
    return jsonify({
        "@odata.type": "#ServiceRoot.v1_5_0.ServiceRoot",
        "Id": "RootService",
        "Name": "Root Service",
        "RedfishVersion": "1.5.0",
        "Systems": {"@odata.id": "/redfish/v1/Systems"},
        "SessionService": {"@odata.id": "/redfish/v1/SessionService"},
        "Links": {
            "Sessions": {"@odata.id": "/redfish/v1/SessionService/Sessions"}
        }
    })

@app.route('/redfish/v1/SessionService')
def session_service():
    return jsonify({
        "@odata.id": "/redfish/v1/SessionService",
        "Name": "Session Service",
        "Status": {"State": "Enabled", "Health": "OK"},
        "Sessions": {"@odata.id": "/redfish/v1/SessionService/Sessions"}
    })

@app.route('/redfish/v1/SessionService/Sessions', methods=['POST'])
def session_login():
    return jsonify({"Id": "mock-session-id"}), 201, {"Location": "/redfish/v1/SessionService/Sessions/mock-session-id", "X-Auth-Token": "mock-token"}

@app.route('/redfish/v1/SessionService/Sessions/<session_id>', methods=['DELETE'])
def session_logout(session_id):
    return '', 204

@app.route('/redfish/v1/Systems')
def systems_collection():
    return jsonify({
        "@odata.type": "#ComputerSystemCollection.ComputerSystemCollection",
        "Name": "Computer System Collection",
        "Members@odata.count": 1,
        "Members": [{"@odata.id": "/redfish/v1/Systems/1"}]
    })

@app.route('/redfish/v1/Systems/1')
def system_detail():
    return jsonify(system_info)

@app.route('/redfish/v1/Chassis/1/Power')
def power_info():
    return jsonify({
        "@odata.id": "/redfish/v1/Chassis/1/Power",
        "Name": "Power",
        "PowerControl": [power_info_data],
        "PowerSupplies": [{
            "MemberId": "0",
            "Manufacturer": "HPE",
            "Model": "800W Flex Slot Platinum",
            "Status": {"State": "Enabled", "Health": "OK"}
        }]
    })

@app.route('/redfish/v1/Managers/1')
def manager_info():
    return jsonify({
        "@odata.id": "/redfish/v1/Managers/1",
        "Name": manager_info_data["Name"],
        "ManagerType": "BMC",
        "FirmwareVersion": manager_info_data["FirmwareVersion"],
        "Status": {"State": "Enabled", "Health": "OK"}
    })

if __name__ == '__main__':
    # Running with SSL for python-ilorest-library compatibility
    app.run(host='0.0.0.0', port=5000, ssl_context=('cert.pem', 'key.pem'))
