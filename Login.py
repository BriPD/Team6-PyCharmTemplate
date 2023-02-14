import tkinter as tk
import mysql.connector
from tkinter import *
import tkinter.messagebox as popupmessagebox
import subprocess


# Connecting to database
con = mysql.connector.connect(host="107.180.1.16",
                                   user="springa2023team6",
                                   password="springa2023team6",
                                   database="springa2023team6")
cursor = con.cursor()


class login(tk.Tk):
    def __init__(self, master=None):
        super().__init__(master)
        self.title("Cyber Devils Login Page")
        self.geometry("573x731")

        # Add the background image
        self.back_image = tk.PhotoImage(file="Journal.png")
        self.back_label = tk.Label(self, image=self.back_image)
        self.back_label.pack(fill="both", expand=True)

        self.intro = tk.Label(self, text="\n\nWELCOME \nPlease login to your account:\n ", font='Times 14 bold',
                              bg="black", fg="white")
        self.intro.place(x=170, y=235)

        # Username Input
        self.userrow = tk.Label(self, text="Username:", bg="black", fg="white")
        self.userrow.place(x=150, y=360)
        self.userrow_entry = tk.Entry(self, width=30)
        self.userrow_entry.place(x=250, y=360)

        # Password Input
        self.passrow = tk.Label(self, text="Password:", bg="black", fg='white')
        self.passrow.place(x=150, y=400)
        self.passrow_entry = tk.Entry(self, show="*", width=30)
        self.passrow_entry.place(x=250, y=400)

        # Login Button
        self.submitbtn = tk.Button(self, text="Login", bg='green', fg='white',
                                   command=self.attempts)
        self.submitbtn.place(x=270, y=450)


    def attempts(self):
        i = 1
        username = self.userrow_entry.get()
        password = self.passrow_entry.get()
        # Validate user
        query = "SELECT * FROM employee WHERE username = %s AND password = %s"
        cursor.execute(query, (username, password))
        person = cursor.fetchone()

        if person:
            popupmessagebox.showinfo("Success", "{} Login Successfully!".format(username))
            subprocess.run(["python", "pitpeakgame.py"])
            self.destroy()
        else:
            self.attempts = 0 + i
            if self.attempts < 3:
                popupmessagebox.showerror("Error", "Invalid username and or password."
                                                   "\nYou have {} attempts left.".format(3 - self.attempts))
                if person:
                    popupmessagebox.showinfo("Success", "{} Login Successfully!".format(username))
                    subprocess.run(["python", "pitpeakgame.py"])
                    self.destroy()
                else:
                    popupmessagebox.showerror("Error", "Too many incorrect login attempts."
                                                   "\nPlease contact Admin.")
                    self.destroy()


# Start App
app = login()
app.mainloop()


# End database connection
cursor.close()
con.close()


# login test credential
# sauer.price
# afcf97aeaa2acfbc9c9f856bcc53744a