from tkinter import *
from pathlib import Path
import os
import webbrowser

window = Tk()
window.title("Cutemail")
window.resizable(0,0)

def send():
    t = to.get()
    s = subject.get()
    e = email.get(1.0, END)
    open("/tmp/email", "w").write(e)
    command = "mail -s '{}' {} < /tmp/email".format(s, t)
    os.system(command)
def compose():
    global to, subject, email
    to = Entry()
    to.grid(column=1, row=3, sticky=W)
    subject = Entry()
    subject.grid(column=1, row=4, sticky=W)
    email = Text()
    email.grid(column=0, row=5, sticky=W)
    Label(window, text="To:").grid(column=0, row=3, sticky=W)
    Label(window, text="Subject:").grid(column=0, row=4, sticky=W)
    Button(window, text="Send", command=send).grid(column=0, row=6, sticky=W)
def change():
    u = username.get()
    open("{}/.cutemail_username".format(Path.home()), "w").write(u)
    webbrowser.open("http://dispostable.com/inbox/{}".format(u))
def check():
    global username
    try:
        open("{}/.cutemail_ran".format(Path.home()))
        webbrowser.open("http://dispostable.com/inbox/{}".format(open("{}/.cutemail_username".format(Path.home()), "r").read()))
    except FileNotFoundError:
        open("{}/.cutemail_ran".format(Path.home()), "w")
        Label(window, text="Username:").grid(column=0, row=3, sticky=W)
        username = Entry()
        username.grid(column=1, row=3, sticky=W)
        Button(window, text="Set", command=change).grid(column=0, row=4, sticky=W)

Label(window, text="Welcome there! What would you like to do today?").grid(column=0, row=0, sticky=W)
Button(window, text="Compose", command=compose).grid(column=0, row=1, sticky=W)
Button(window, text="Check", command=check).grid(column=0, row=2, sticky=W)

window.mainloop()