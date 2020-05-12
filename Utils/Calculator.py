#!/usr/bin/python

"""
"""
import time


# ---------------------------------------------------------


def open_calc(device):
    device.wakeup()
    device.press.home()
    wait()
    device(text='Calculator', className='android.widget.TextView').click()


def make_operation(device, operation, result):
    device(resourceId='com.sec.android.app.popupcalculator:id/calc_keypad_btn_clear'
           , className='android.widget.Button').click()
    for i in operation:
        if i == '0':
            device(resourceId='com.sec.android.app.popupcalculator:id/calc_keypad_btn_00'
                   , className='android.widget.Button').click()
        elif i == '1':
            device(resourceId='com.sec.android.app.popupcalculator:id/calc_keypad_btn_01'
                   , className='android.widget.Button').click()
        elif i == '2':
            device(resourceId='com.sec.android.app.popupcalculator:id/calc_keypad_btn_02'
                   , className='android.widget.Button').click()
        elif i == '3':
            device(resourceId='com.sec.android.app.popupcalculator:id/calc_keypad_btn_03'
                   , className='android.widget.Button').click()
        elif i == '4':
            device(resourceId='com.sec.android.app.popupcalculator:id/calc_keypad_btn_04'
                   , className='android.widget.Button').click()
        elif i == '5':
            device(resourceId='com.sec.android.app.popupcalculator:id/calc_keypad_btn_05'
                   , className='android.widget.Button').click()
        elif i == '6':
            device(resourceId='com.sec.android.app.popupcalculator:id/calc_keypad_btn_06'
                   , className='android.widget.Button').click()
        elif i == '7':
            device(resourceId='com.sec.android.app.popupcalculator:id/calc_keypad_btn_07'
                   , className='android.widget.Button').click()
        elif i == '8':
            device(resourceId='com.sec.android.app.popupcalculator:id/calc_keypad_btn_08'
                   , className='android.widget.Button').click()
        elif i == '9':
            device(resourceId='com.sec.android.app.popupcalculator:id/calc_keypad_btn_09'
                   , className='android.widget.Button').click()
        elif i == '.':
            device(resourceId='com.sec.android.app.popupcalculator:id/calc_keypad_btn_dot'
                   , className='android.widget.Button').click()
        elif i == '*':
            device(resourceId='com.sec.android.app.popupcalculator:id/calc_keypad_btn_mul'
                   , className='android.widget.Button').click()
        elif i == '/':
            device(resourceId='com.sec.android.app.popupcalculator:id/calc_keypad_btn_div'
                   , className='android.widget.Button').click()
        elif i == '-':
            device(resourceId='com.sec.android.app.popupcalculator:id/calc_keypad_btn_sub'
                   , className='android.widget.Button').click()
        elif i == '+':
            device(resourceId='com.sec.android.app.popupcalculator:id/calc_keypad_btn_add'
                   , className='android.widget.Button').click()
        wait(0.2)
    local_result = device(resourceId='com.sec.android.app.popupcalculator:id/calc_tv_result').__getattr__('text')
    if local_result is None:
        local_result = 'None'
    device(resourceId='com.sec.android.app.popupcalculator:id/calc_keypad_btn_equal'
           , className='android.widget.Button').click()
    if local_result == result:
        print("Test Passed:\n\tOperation: {0}\n\tExpected Result: {1}\n\tActual Result: {2}"
              .format(operation, result, local_result))
    else:
        print("Test Failed - Wrong Result:\n\tOperation: {0}\n\tExpected Result: {1}\n\tActual Result: {2}"
              .format(operation, result, local_result))


def wait(sec=0.1):
    time.sleep(sec)
