from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice
import commands
import sys

# starting script
print "start"

# connection to the current device, and return a MonkeyDevice object
device = MonkeyRunner.waitForConnection()


# List all packages installed

installed_packages = device.shell('pm list packages -f -3')
for app in installed_packages.split():
    package_name = app.split("=")[1]
    apk_path = device.shell('pm path ' + package_name)
    if apk_path.startswith('package:'):
        print package_name + " already installed."
        print "Apk Path is " + apk_path.split(":")[1]
    else:
        print package_name + " not installed"
    MonkeyRunner.sleep(2)
    
'''
apk_path = device.shell('pm path com.erigo.cowise')
if apk_path.startswith('package:'):
    print "Cowise already installed."
else:
    print "Cowise not installed, installing APKs..."
    device.installPackage('myapp.apk')

print "launching myapp..."
device.startActivity(component='com.erigo.cowise/com.erigo.cowise.SplashScreen')

#screenshot
MonkeyRunner.sleep(10)

#sending an event which simulate a click on the menu button
device.touch(591, 1660, MonkeyDevice.DOWN_AND_UP)
'''
print "end of script"
