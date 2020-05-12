#!/usr/bin/python

"""

"""
from subprocess import check_output
import time
import datetime
from uiautomator import Device
import pytz
import Utils.Serial as Serial


# ---------------------------------------------------------


def turn_wifi_on(device):
    device.wakeup()
    device.press.home()
    device.open.quick_settings()
    wait()
    device(resourceId='com.android.systemui:id/settings_button', className='android.widget.ImageButton').click()
    wait()
    device(text='Connections').click()
    wait()
    wifi_opt = device(resourceId='android:id/switch_widget', className='android.widget.Switch')
    if wifi_opt.__getattr__('text') == 'On':
        print('Wifi is already turned on')
    else:
        wifi_opt.click()
        print('Wifi has been turned on  successfully')
    device.press.home()
    return


def wait(sec=0.1):
    time.sleep(sec)


# ---------------------------------------------------------------------------


if __name__ == "__main__":
    serial = Serial.read_serial()
    start_ts_pst = str(datetime.datetime.now(pytz.timezone('US/Pacific')).strftime('"%m-%d-%y %H:%M:%S.%f"'))
    print('serial: %s' % serial)

    try:
        d = Device(serial)

        print("** Script Turn On Wifi **")
        turn_wifi_on(d)

    except Exception as ex:
        print(ex)
    finally:

        stop_ts = datetime.datetime.now()
        stop_ts_pst = str(datetime.datetime.now(pytz.timezone('US/Pacific')).strftime('"%m-%d-%y %H:%M:%S.%f"'))

        print("--------------- RESULTS ---------------")
        print('test start:  %s ' % start_ts_pst)
        print('test end  :  %s' % stop_ts_pst)
