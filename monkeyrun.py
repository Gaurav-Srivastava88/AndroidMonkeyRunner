#! /usr/bin

import threading
import os
from util import utility
from interact_apps import interact_with_apps


class monkeyThread (threading.Thread):
    def __init__(self, device_name):
        self.device_name = device_name
        threading.Thread.__init__(self)

    def run(self):
        interact_with_apps.initialize_device_for_testing(self.device_name)

        apk_names = [fileName for fileName in os.listdir("apps") if fileName.endswith(".apk")]

        for apk in apk_names:
            # Find the app id for the apk file. For example: PrivacyProxy.apk, io.privacyproxy
            app_id = interact_with_apps.get_app_id(apk)
            print 'Running tests for ' + apk
            print app_id

            # Once we have the app id check is app is already installed otherwise install using the apk file
            interact_with_apps.check_app_installed(app_id, apk)

            # After the previous step the app is now installed on the device and we can ask monkey to run it using app id
            # and do random strokes once app is launched
            interact_with_apps.initialize_test(app_id)


def main():
    # starting script
    print "start of script \n"

    # Get all devices connected to laptop via USB
    connected_devices = utility.get_connected_devices()
    # print 'device ids: \n' + connected_devices

    threads = []
    for device in connected_devices:
        print 'starting for Device: ' + device
        thread = monkeyThread(device)
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

    print "\nend of script"

if __name__ == '__main__':
    main()