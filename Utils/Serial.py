from subprocess import check_output


# ---------------------------------------------------------------------------


def read_serial():
    output = check_output(['adb', 'devices'])
    lines = output.splitlines()
    first_dev = lines[1].split()[0]
    return first_dev

