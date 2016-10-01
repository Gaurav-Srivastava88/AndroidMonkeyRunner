from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice
import commands
import sys
import random


def get_launcher_activity(package_name):
    tmp = device.shell('pm dump ' + package_name + ' | grep -A 1 MAIN | grep -i -w ' + package_name) 
    #print tmp

    print tmp
    
    for c in tmp.split(" "):
        if package_name in c:
            print c
            launcher_activity = c.split()[0]
            print launcher_activity
            break
    return launcher_activity
	
	
def get_rand_app(installed_packages):
    all_apps = installed_packages.split()
    max = len(all_apps)
	
    sample_no = random.sample(range(1, max), 5)
    sample_apps = {}
    for no in sample_no:
        sample_apps[all_apps[no]] = ""
    return sample_apps    
    
def stop_app(package_name):
    # Simulates Closing an application by user
    MonkeyRunner.sleep(5)
        
    device.shell('am force-stop ' + package_name)


def remove_one_recent_app():
    MonkeyRunner.sleep(2)
    device.press('KEYCODE_APP_SWITCH', MonkeyDevice.DOWN_AND_UP)

    MonkeyRunner.sleep(1)
    device.drag((350, 620), (13, 620), 0.5, 50)


# starting script
print "start"

# connection to the current device, and return a MonkeyDevice object
device = MonkeyRunner.waitForConnection()

installed_packages = device.shell('pm list packages -f -3')

sampled_apps = get_rand_app(installed_packages)

testing_apps = {}

for app in sampled_apps:
    package_name = app.split("=")[1]
    print package_name
    testing_apps[package_name] = get_launcher_activity(package_name)

print testing_apps

'''
for app in testing_apps:
    device.startActivity(component=testing_apps[app])
    MonkeyRunner.sleep(5)

#stop_app('com.erigo.cowise')

MonkeyRunner.sleep(5)
remove_one_recent_app()
'''

# List all packages installed
'''
for app in installed_packages.split():
    apk_path = device.shell('pm path ' + package_name)
    if apk_path.startswith('package:'):
        print package_name + " already installed."
        print "Apk Path is " + apk_path.split(":")[1]
    else:
        print package_name + " not installed"
    MonkeyRunner.sleep(2)
''' 
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
