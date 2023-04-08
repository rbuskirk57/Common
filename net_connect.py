import network
from time import sleep

def connect(ssid, password):
    #Connect to WLAN
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    max_count = 20
    ip = '-1'
    # set static IP - put this in the secrets file for future)
    #wlan.ifconfig(('192.168.40.57', '255.255.252.0', '192.168.42.1', '8.8.8.8'))
    wlan.connect(ssid, password)
    
    while max_count > 0:
        print('Waiting for connection...')
        sleep(1)
        if wlan.isconnected():
            ip = wlan.ifconfig()[0]
            print(f'Connected on {ip}')
            break
        else:
            max_count -= 1

    if not wlan.isconnected():
        print("Network connection failed")
        #ip = -1
    return ip