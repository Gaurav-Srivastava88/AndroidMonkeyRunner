from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice
import commands
import sys

# starting script
print "start"

# connection to the current device, and return a MonkeyDevice object
device = MonkeyRunner.waitForConnection()

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

print "end of script"
