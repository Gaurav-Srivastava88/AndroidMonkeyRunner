import sys
import subprocess
from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice


device = None

def stop_app(package_name):
    # Simulates Closing an application by user
    MonkeyRunner.sleep(2)
    device.shell('am force-stop ' + package_name)


def remove_one_recent_app():
    MonkeyRunner.sleep(2)
    device.press('KEYCODE_APP_SWITCH', MonkeyDevice.DOWN_AND_UP)

    MonkeyRunner.sleep(1)
    device.drag((360, 620), (13, 620), 2.0, 10)


def launch_app(app_launcher_activity):
    print 'launching ' + app_launcher_activity
    device.startActivity(component=app_launcher_activity)


def get_launcher_activity(package_name):
    tmp = device.shell('pm dump ' + package_name + ' | grep -A 1 MAIN | grep -i -w ' + package_name)
    print tmp
    for c in tmp.split(" "):
        if package_name in c:
            print c
            launcher_activity = c.split()[0]
            return launcher_activity


def do_random_keystrokes():
    MonkeyRunner.sleep(1)
    device.touch(591, 60, MonkeyDevice.DOWN_AND_UP)
    MonkeyRunner.sleep(1)
    device.drag((650, 620), (13, 620), 0.5, 50)
    MonkeyRunner.sleep(1)
    device.touch(791, 491, MonkeyDevice.DOWN_AND_UP)
    MonkeyRunner.sleep(1)
    device.drag((35, 620), (713, 620), 0.5, 50)
    MonkeyRunner.sleep(1)
    device.touch(0, 500, MonkeyDevice.DOWN_AND_UP)
    MonkeyRunner.sleep(1)
    device.touch(200, 120, MonkeyDevice.DOWN_AND_UP)
    MonkeyRunner.sleep(1)
    device.touch(100, 520, MonkeyDevice.DOWN_AND_UP)
    MonkeyRunner.sleep(1)
    device.touch(391, 1260, MonkeyDevice.DOWN_AND_UP)
    MonkeyRunner.sleep(1)
    device.drag((450, 320), (13, 620), 0.5, 50)
    MonkeyRunner.sleep(1)
    device.touch(191, 491, MonkeyDevice.DOWN_AND_UP)
    MonkeyRunner.sleep(1)
    device.drag((235, 620), (713, 620), 0.5, 50)
    MonkeyRunner.sleep(1)
    device.touch(300, 10, MonkeyDevice.DOWN_AND_UP)
    MonkeyRunner.sleep(1)
    device.touch(200, 120, MonkeyDevice.DOWN_AND_UP)
    MonkeyRunner.sleep(1)
    device.touch(100, 320, MonkeyDevice.DOWN_AND_UP)
    MonkeyRunner.sleep(1)
    device.touch(491, 260, MonkeyDevice.DOWN_AND_UP)
    MonkeyRunner.sleep(1)
    device.drag((250, 620), (13, 620), 0.5, 50)
    MonkeyRunner.sleep(1)
    device.touch(491, 491, MonkeyDevice.DOWN_AND_UP)
    MonkeyRunner.sleep(1)
    device.drag((335, 620), (713, 620), 0.5, 50)
    MonkeyRunner.sleep(1)
    device.touch(0, 180, MonkeyDevice.DOWN_AND_UP)
    MonkeyRunner.sleep(1)
    device.touch(200, 120, MonkeyDevice.DOWN_AND_UP)
    MonkeyRunner.sleep(1)
    device.touch(100, 320, MonkeyDevice.DOWN_AND_UP)


def check_app_installed(app_id, app_apk):
    apk_path = device.shell('pm path ' + app_id)
    if apk_path.startswith('package:'):
        print app_id + " already installed."
    else:
        print app_id + " not installed, installing APK..."
        device.installPackage('apps/' + app_apk)


def initialize_test(app_id):
    # From the app id passed find the launcher activity for the app
    launcher_activity  = get_launcher_activity(app_id)

    # Pass the found launch activity to start the app
    launch_app(launcher_activity)
    MonkeyRunner.sleep(8)

    # After the app is successfully launched start doing the random strokes
    do_random_keystrokes()
    MonkeyRunner.sleep(2)

    # On completion of random strokes process stop the app
    stop_app(app_id)
    MonkeyRunner.sleep(5)

    # Once the app is stopped we can use swipe action from monkey an remove app from recent apps
    remove_one_recent_app()


def initialize_device_for_testing(device_name):
    # connection to the current device, and return a MonkeyDevice object
    global device
    device = MonkeyRunner.waitForConnection(30.0, device_name)
    if device is None:
        print "Initialization Failed."
        sys.exit()
    else:
        print "Device Initialization Successful"


def get_app_id(apk_name):
    tmp = subprocess.Popen('aapt dump badging apps/' + apk_name + ' | awk -v FS=\"\'\" \'/package: name=/{print $2}\'', shell=True, stdout=subprocess.PIPE)
    return tmp.communicate()[0].rstrip()
