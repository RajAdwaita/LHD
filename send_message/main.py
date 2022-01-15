import requests

from tkinter import *
from tkinter.messagebox import *


def send_sms(number, message):
    url = "https://www.fast2sms.com/dev/bulkV2"

    params = {
        'authorization': 'nAxcz3v5etgblwCrR6MV7EIP0q2G8F1mKHduNhDTSULJQBay4kf6QD1FCZSPhvELsAOTk5iro3ygBpjb',
        'sender_id': 'FastSM',
        'message': message,
        'route': 'p',
        'numbers': number,
        'language': 'english'
    }

    response = requests.get(url, params=params)
    dic = response.json()
    print(dic)
    # print(type(dic))
    return dic.get('return')


def btn_click():
    num = textNumber.get()
    msg = textMessage.get("1.0", END)

    r = send_sms(num, msg)

    if(r == True):
        showinfo("Success", "Message sent successfully")
    else:
        showinfo("Error", "Message not sent")


root = Tk()
root.title("Send SMS")

root.geometry("400x400")
font = ("Arial", 20, "bold")

textNumber = Entry(root, font=font)
# textNumber.grid(row=0, column=1)
textNumber.pack(fill=X, pady=20)

textMessage = Text(root)
textMessage.pack(fill=X)

sendBtn = Button(root, text="Send TEXT", command=btn_click,
                 font=font, bg="green", fg="white")

sendBtn.pack()
root.mainloop()
