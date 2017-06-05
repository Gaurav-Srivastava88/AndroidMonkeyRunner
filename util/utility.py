import subprocess

def get_connected_devices():
    tmp = subprocess.Popen('adb devices | grep -w "device" | awk \'{print $1;}\'', shell=True, stdout=subprocess.PIPE, stderr=None)
    text = tmp.communicate()[0].rstrip()
    return text.split('\n')