import sys
import tkinter as tk
from tkinter import PhotoImage
from tkinter import Text
from datetime import datetime, date
import mysql.connector
import tkinter.messagebox as popupmessagebox

# login test credential
# sauer.price
# afcf97aeaa2acfbc9c9f856bcc53744a

# Get today's date
date = date.today()

conn = mysql.connector.connect(host="107.180.1.16",
                                   user="springa2023team6",
                                   password="springa2023team6",
                                   database="springa2023team6")

# Creating a cursor object using the cursor() method
cursor = conn.cursor()


def store_pit_text(pittext, peaktext):
    global pit_text_content, peak_text_content, time
    now = datetime.now()
    time = now.strftime("%H:%M:%S")
    pit_text_content = pittext.get("1.0", 'end-1c')
    print("Pit text: "+pit_text_content)
    peak_text_content = peaktext.get("1.0", 'end-1c')
    print("Peak text: "+peak_text_content)

    pitnpeak_page.destroy()

    # Preparing SQL query to INSERT a record into the database.
    insert_stmt = (
        "INSERT INTO feedback(feedID, date, time, user, pittext, peaktext)"
        "VALUES (%s, %s, %s, %s, %s, %s)"
    )

    data = (" ", date, time, username, pit_text_content, peak_text_content)

    try:
        # executing the sql command
        cursor.execute(insert_stmt, data)
        # commit changes in database
        conn.commit()
    except:
        conn.rollback()

    thank_you_page = tk.Tk()
    thank_you_page.geometry("800x770")
    thank_you_page.title("Thank You Page")

    # Create a label for the title
    thank_you_title = tk.Label(thank_you_page, text="Thank you for your feedback!", font=("Helvetica", 24))
    thank_you_title.pack(pady=5)

    # Create a PhotoImage object for the background image
    image = PhotoImage(file="mountain.png")

    # Create a label to hold the image
    background_label = tk.Label(thank_you_page, image=image)
    background_label.pack(fill="both", expand=True)

    thank_you_page.mainloop()


def welcomepage():
    global welcome
    # app.destroy()
    # Create the main window
    welcome = tk.Tk()
    welcome.geometry("800x770")
    welcome.title("Welcome page")

    # Create a label for the title
    title = tk.Label(welcome, text="Game: Pit and Peak of the Day", font=("Helvetica", 24))
    title.pack(pady=5)

    # Create a label to display today's date
    date_label = tk.Label(welcome, text="Today's date: " + date.strftime("%B %d, %Y"), font=("Helvetica", 14))
    date_label.pack(pady=5)

    # Create a button
    enter_button = tk.Button(welcome, text="Enter", font=("Helvetica", 16), command=go_to_pit_page)
    enter_button.pack(pady=5)

    # # Create a PhotoImage object for the background image
    # mtn_image = tk.PhotoImage(file="mountain.png")
    #
    # # Create a label to hold the image
    # background_label = tk.Label(welcome, image=mtn_image)
    # background_label.pack(fill="both", expand=True)

    photo = PhotoImage(file="mountain.png")

    label = tk.Label(welcome, image=photo)
    label.image = photo  # keep a reference!
    label.pack(fill="both", expand=True)


def login():
    global username, tries
    tries = tries + 1
    username = userrow_entry.get()
    password = passrow_entry.get()
    # Validate user
    query = "SELECT * FROM employee WHERE username = %s AND password = %s"
    cursor.execute(query, (username, password))
    person = cursor.fetchone()

    if person:
        popupmessagebox.showinfo("Success", "{} Login Successfully!".format(username))
        app.destroy()
        welcomepage()
    elif tries>2:
        popupmessagebox.showerror("Error", "Too many incorrect login attempts."
                                           "\nPlease contact Admin. Goodbye...")
        sys.exit()
    else:
        print(tries)
        popupmessagebox.showerror("Error", "Login credentials incorrect. Try again.")


def go_to_pit_page():
    welcome.destroy()
    global pitnpeak_page
    pitnpeak_page = tk.Tk()
    pitnpeak_page.geometry("800x770")
    pitnpeak_page.title("Game Feedback Page")

    # Create a label for the title
    pit_title = tk.Label(pitnpeak_page, text="Pit: What were the challenging part(s) of the day?", font=("Helvetica", 24))
    pit_title.pack(pady=5)

    # Create a text box for user input
    pit_text = Text(pitnpeak_page, height=10, width=40)
    pit_text.pack(pady=5)

    # Create a label for the title
    peak_title = tk.Label(pitnpeak_page, text="Peak: What were the best part(s) of the day?", font=("Helvetica", 24))
    peak_title.pack(pady=5)

    # Create a text box for user input
    peak_text = Text(pitnpeak_page, height=10, width=40)
    peak_text.pack(pady=5)

    # Create a submit button
    submit_button = tk.Button(pitnpeak_page, text="Submit", font=("Helvetica", 16), command=lambda: store_pit_text(pit_text, peak_text))
    submit_button.pack(pady=5)

    pitnpeak_page.mainloop()


# Create the main window
app = tk.Tk()
app.title("Cyber Devils Login Page")
app.geometry("573x731")

# Add the background image
back_image = tk.PhotoImage(file="Journal.png")
back_label = tk.Label(app, image=back_image)
back_label.pack(fill="both", expand=True)

intro = tk.Label(app, text="\n\nWELCOME \nPlease login to your account:\n ", font='Times 14 bold',
                      bg="black", fg="white")
intro.place(x=170, y=235)

tries = 0

# Username Input
userrow = tk.Label(app, text="Username:", bg="black", fg="white")
userrow.place(x=150, y=360)
userrow_entry = tk.Entry(app, width=30)
userrow_entry.place(x=250, y=360)

# Password Input
passrow = tk.Label(app, text="Password:", bg="black", fg='white')
passrow.place(x=150, y=400)
passrow_entry = tk.Entry(app, show="*", width=30)
passrow_entry.place(x=250, y=400)

# Login Button
submitbtn = tk.Button(app, text="Login", bg='green', fg='black', command=login)
submitbtn.place(x=270, y=450)

# Start the main event loop
app.mainloop()

# login test credential
# sauer.price
# afcf97aeaa2acfbc9c9f856bcc53744a