from uiautomator import Device
import datetime
import pytz
import Utils.Calculator as Calculator
import Utils.Serial as Serial


# ---------------------------------------------------------------------------


if __name__ == "__main__":
    serial = Serial.read_serial()
    start_ts_pst = str(datetime.datetime.now(pytz.timezone('US/Pacific')).strftime('"%m-%d-%y %H:%M:%S.%f"'))
    f = open("operation.txt", "r")
    print('serial: %s' % serial)

    try:
        print("** Calculator Script **")
        d = Device(serial)
        Calculator.open_calc(d)
        for x in f:
            operation = x.split()[0]
            res = x.split()[1]
            Calculator.make_operation(d, operation, res)
            Calculator.wait(0.5)

    except Exception as ex:
        print(ex)

    finally:
        stop_ts = datetime.datetime.now()
        stop_ts_pst = str(datetime.datetime.now(pytz.timezone('US/Pacific')).strftime('"%m-%d-%y %H:%M:%S.%f"'))

        print("--------------- RESULTS ---------------")
        print('test start:  %s ' % start_ts_pst)
        print('test end  :  %s' % stop_ts_pst)