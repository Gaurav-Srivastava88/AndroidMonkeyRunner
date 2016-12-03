from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice
import commands
import sys
import random

sample_apps = {
    "com.facebook.orca":"com.facebook.orca/.auth.StartScreenActivity",
    "com.wishabi.flipp":"com.wishabi.flipp/.app.LauncherActivity",
    "com.pandora.android":"com.pandora.android/.Main",
    
    #"com.bhvr.lhh":"com.bhvr.lhh/com.bhvr.urlschememanagementlibrary.UrlSchemeManagement",
    #"com.erepubliklabs.worldatwar":"com.erepubliklabs.worldatwar/com.prime31.UnityPlayerNativeActivity",
    #"com.kiloo.subwaysurf":"com.kiloo.subwaysurf/com.kiloo.unityutilities.UnityPluginActivity",
    #"com.google.android.apps.fireball":"com.google.android.apps.fireball/.ui.conversationlist.ConversationListActivity",
    #"com.hulu.plus":"com.hulu.plus/com.hulu.plusx.activity.Root",
    #"com.cmcm.live":"com.cmcm.live/com.cmcm.cmlive.activity.SplashActivity",
    #"air.com.hypah.io.slither":"air.com.hypah.io.slither/.AppEntry"
    "kik.android":"kik.android/.chat.activity.IntroActivity"
}


def stop_app(package_name):
    # Simulates Closing an application by user
    MonkeyRunner.sleep(5)
        
    device.shell('am force-stop ' + package_name)


def remove_one_recent_app():
    MonkeyRunner.sleep(2)
    device.press('KEYCODE_APP_SWITCH', MonkeyDevice.DOWN_AND_UP)

    MonkeyRunner.sleep(1)
    device.drag((350, 620), (13, 620), 0.5, 50)


def launch_app(app_launcher_activity):
    print "launching " + app_launcher_activity
    device.startActivity(component=app_launcher_activity)


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
        
    
# starting script
print "start"

# connection to the current device, and return a MonkeyDevice object
device = MonkeyRunner.waitForConnection()

i=0
while(i < 50):
    i = i+1
    for app in sample_apps:
        launch_app(sample_apps[app])
        MonkeyRunner.sleep(8)
        do_random_keystrokes()
        MonkeyRunner.sleep(2)
        stop_app(app)
        MonkeyRunner.sleep(5)
        remove_one_recent_app()
    
print "end of script"
