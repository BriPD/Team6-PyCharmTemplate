import tkinter as tk
import mysql.connector
from tkinter import *
import tkinter.messagebox as popupmessagebox


# submit button function
def submit():
    # Database connection
    db = mysql.connector.connect(host="107.180.1.16",
                                   user="springa2023team6",
                                   password="springa2023team6",
                                   database="springa2023team6")
    cursor = db.cursor(dictionary=True)
    # Query statement
    cursor.execute("SELECT username, password FROM employee")
    result = cursor.fetchone()

    # Invalid login
    if result == None:
        popupmessagebox.showerror("Error", "Invalid User Name And Or Password")

    # Successful login message
    else:
        popupmessagebox.showinfo("Success", "Login Successfully")

    db.close()
    cursor.close()


# Layout and styling
win = tk.Tk()
win.geometry("300x360")
win.title("Cyber Devils Login Page")

win.configure(bg='black')

intro = Label(win, text=" Please Login To Your Account ", font='Times 14 bold', bg='green', fg='white')
intro.place(x=20, y=40)

# Login input
userrow = tk.Label(win, text="Username", font='bold 10', bg='black', fg='white')
userrow.place(x=50, y=110)

user = tk.Entry(win, width=35)
user.place(x=130, y=110, width=120)

passrow = tk.Label(win, text="Password", font='bold 10', bg='black', fg='white')
passrow.place(x=50, y=140)

emppass = tk.Entry(win, width=35, show="*")
emppass.place(x=130, y=140, width=120)

submitbtn = tk.Button(win, text="Login", font='Times 10',
                      bg='green', fg='white', command=submit)
submitbtn.place(x=120, y=205, width=55)

win.mainloop()


# login test credential
# sauer.price
# afcf97aeaa2acfbc9c9f856bcc53744a