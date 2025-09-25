#Code adapted from:
# https://projects.raspberrypi.org/en/projects/get-started-pico-w/2 for wifi connectivity
# https://forums.raspberrypi.com/viewtopic.php?t=340568 for webscraping


from urllib.urequest import urlopen
import network
import config
import time 
import sys


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
        page = urlopen(url)
        html_bytes = page.read()
        html = html_bytes.decode("utf-8")
        print(html)
        start_index = html.find("<title>") + len("<title>")
        end_index = html.find("</title>")
        title = html[start_index:end_index]
        print(title)
            

except Exception as e:
    print('Error:', e)

    
   


