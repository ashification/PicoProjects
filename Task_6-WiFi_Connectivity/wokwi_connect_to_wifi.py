# Picozero as a library import module is included as a python file 
# As Woki was having issues importing it by default
# AS part of the pico hardware steps this is imported without needing to include the file
# As the urllib.request library was unavailbable code was take and adapted from here https://wokwi.com/projects/432027273041892353

print("Hello World")


import network
import config
import time 
import sys
print("Libraries Declared")

#Declare GPIO usage  

print("GPIO Pins Declared")

def http_get(url):
    import socket
    _, _, host, path = url.split('/', 3)
    print(url.split('/', 3))
    addr = socket.getaddrinfo(host, 80)[0][-1]
    print(addr)
    s = socket.socket()
    s.connect(addr)
    s.send(bytes('GET /%s HTTP/1.0\r\nHost: %s\r\n\r\n' % (path, host), 'utf8'))
    while True:
        data = s.recv(100)
        if data:
            print(str(data, 'utf8'), end='')
        else:
            break
    s.close()

def initialize_wifi(ssid, password):
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)

    # Connect to the network
    wlan.connect(ssid, password)

    # Wait for Wi-Fi connection
    connection_timeout = 10
    while connection_timeout > 0:
        if wlan.status() >= 3:
            break
        connection_timeout -= 1
        print('Waiting for Wi-Fi connection...')
        time.sleep(1)

    # Check if connection is successful
    if wlan.status() != 3:
        return False
    else:
        print('Connection successful!')
        network_info = wlan.ifconfig()
        print('IP address:', network_info[0])
        return True

try:
    if not initialize_wifi(config.wifi_ssid, config.wifi_password):
        print('Error connecting to the network... exiting program')
    else:
        #Webscraping to validate internet connection
        url = "http://olympus.realpython.org/profiles/aphrodite"
        html = http_get(url)
        print(html)
            

except Exception as e:
    print('Error:', e)

