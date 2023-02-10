import tkinter as tk
import mysql.connector
from tkinter import *
import tkinter.messagebox as popupmessagebox


# Connecting to database
con = mysql.connector.connect(host="107.180.1.16",
                                   user="springa2023team6",
                                   password="springa2023team6",
                                   database="springa2023team6")
cursor = con.cursor()


class login(tk.Tk):
    def __init__(self):
        super().__init__()
        # self.attempts = 0
        self.title("Cyber Devils Login Page")
        self.geometry("300x360")
        self.configure(bg='black')
        self.intro = Label(self, text="\n\nW E L C O M E \nPlease Login To Your Account\n ", font='Times 14 bold', bg='black',
                      fg='white')
        self.intro.place(x=20, y=40)
        self.intro.pack()

        # Username Input
        self.userrow = tk.Label(self, text="Username:", font='bold 10', bg='black', fg='white')
        self.userrow.place(x=50, y=110)
        self.userrow.pack()
        self.userrow_entry = tk.Entry(self, width=35, bg='green')
        self.userrow_entry.place(x=130, y=110, width=120)
        self.userrow_entry.pack()

        # Password Input
        self.passrow = tk.Label(self, text="\nPassword:", font='bold 10', bg='black', fg='white')
        self.passrow.place(x=50, y=140)
        self.passrow.pack()
        self.passrow_entry = tk.Entry(self, width=35, show="*", bg='green')
        self.passrow_entry.place(x=130, y=140, width=120)
        self.passrow_entry.pack()

        # Login Button
        self.submitbtn = tk.Button(self, text="Login", font='Times 10',
                              bg='green', fg='white', command=self.attempts)
        self.submitbtn.place(x=150, y=205, width=55)
        self.submitbtn.pack()

    def attempts(self):
        username = self.userrow_entry.get()
        password = self.passrow_entry.get()
        # Validate user
        query = "SELECT * FROM employee WHERE username = %s AND password = %s"
        cursor.execute(query, (username, password))
        person = cursor.fetchone()
        if person:
            popupmessagebox.showinfo("Success", "{} Login Successfully!".format(username))
        else:
            self.attempts = 0
            if self.attempts < 3:
                # for i in range(3):
                popupmessagebox.showerror("Error", "Invalid username and or password."
                                                   "\nYou have {} attempts left.".format(3 - self.attempts))
                # if person:
                #     popupmessagebox.showinfo("Success", "Login Successfully!")
            else:
                popupmessagebox.showerror("Error", "Too many incorrect login attempts."
                                                   "\nPlease try again later.")
                self.destroy()


# Start App
gui = login()
gui.mainloop()


# End database connection
cursor.close()
con.close()


# login test credential
# sauer.price
# afcf97aeaa2acfbc9c9f856bcc53744a