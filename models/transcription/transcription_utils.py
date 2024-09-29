from pyaudio import PyAudio

def getInputDevices():
    devices = {}
    p = PyAudio()
    for host_index in range(0, p.get_host_api_count()):
        host = p.get_host_api_info_by_index(host_index)
        for device_index in range(0, p.get_host_api_info_by_index(host_index)['deviceCount']):
            device = p.get_device_info_by_host_api_device_index(host_index, device_index)
            if device["maxInputChannels"] > 0:
                if host["name"] in devices.keys():
                    devices[host["name"]].append(device)
                else:
                    devices[host["name"]] = [device]
    if len(devices) == 0:
        devices = {"NoHost": [{"name": "NoDevice"}]}
    return devices

def getDefaultInputDevice():
    p = PyAudio()
    api_info = p.get_default_host_api_info()
    defaultInputDevice = api_info["defaultInputDevice"]

    for host_index in range(0, p.get_host_api_count()):
        host = p.get_host_api_info_by_index(host_index)
        for device_index in range(0, p.get_host_api_info_by_index(host_index)['deviceCount']):
            device = p.get_device_info_by_host_api_device_index(host_index, device_index)
            if device["index"] == defaultInputDevice:
                return {"host": host, "device": device}
    return {"host": {"name": "NoHost"}, "device": {"name": "NoDevice"}}

def getOutputDevices():
    devices = []
    p = PyAudio()
    for host_index in range(0, p.get_host_api_count()):
        host = p.get_host_api_info_by_index(host_index)
        for device_index in range(0, p.get_host_api_info_by_index(host_index)['deviceCount']):
            device = p.get_device_info_by_host_api_device_index(host_index, device_index)
            if device["name"] == "VB-Cable":
                devices.append(device)

    if len(devices) == 0:
        devices = [{"name": "NoDevice"}]
    return devices

def getDefaultOutputDevice():
    p = PyAudio()
    for host_index in range(0, p.get_host_api_count()):
        host = p.get_host_api_info_by_index(host_index)
        for device_index in range(0, p.get_host_api_info_by_index(host_index)['deviceCount']):
            device = p.get_device_info_by_host_api_device_index(host_index, device_index)
            if device["name"] == "VB-Cable":
                return {"device": device}
    return {"device": {"name": "NoDevice"}}

if __name__ == "__main__":
    print("getOutputDevices()", getOutputDevices())
    print("getDefaultOutputDevice()", getDefaultOutputDevice())