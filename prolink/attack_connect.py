import time
import subprocess
import platform

def connect_to_open_wifi(ssid):
    os_name = platform.system()
    print(f"Attempting to connect to '{ssid}' on {os_name}...")

    while True:
        if os_name == "Windows":
            # Windows command to connect to an already known/added open network profile
            # An open network profile must be created first (see Windows section below)
            command = f'netsh wlan connect name="{ssid}" interface=Wi-Fi'
        elif os_name == "Linux":
            # Linux command using nmcli
            command = f'nmcli device wifi connect "{ssid}" ifname wlxec086b1c9db7'
            # Note: 'wlan0' might need to be adjusted based on your interface name
        else:
            print(f"Unsupported OS: {os_name}")
            return

        try:
            # Execute the command
            result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
            print(f"Connection command executed. Output: {result.stdout}")
            # You might need additional logic to verify connection success (e.g., check IP address)

        except subprocess.CalledProcessError as e:
            print(f"Connection failed: {e.stderr}")
        except Exception as e:
            print(f"An error occurred: {e}")

        # Wait a bit before the next attempt
        time.sleep(1)

# Replace 'YOUR_SSID' with the name of the open Wi-Fi network
connect_to_open_wifi('PROLiNK-4828')
