from pynput.keyboard import Key, Listener


def on_press(key):
    global loggedKeys
    if key == Key.shift or key == Key.ctrl_l or key == Key.ctrl_r or key == Key.shift_r:
        print('{0} Pressed'.format(key))
    else:
        print('{0}'.format(key))

def on_release(key):
    global loggedKeys
    if key == Key.shift or key == Key.ctrl_l or key == Key.ctrl_r or key == Key.shift_r:
        print('{0} released'.format(key))
    if key == Key.esc:
        exit(0)

with Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()