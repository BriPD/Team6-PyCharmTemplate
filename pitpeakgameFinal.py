import random
import sys
import tkinter as tk
from datetime import datetime, date
import mysql.connector
import tkinter.messagebox as popupmessagebox
from PIL import Image, ImageTk

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
        welcome_page()
    elif tries>2:
        popupmessagebox.showerror("Error", "Too many incorrect login attempts."
                                           "\nPlease contact Admin. Goodbye...")
        sys.exit()
    else:
        print(tries)
        popupmessagebox.showerror("Error", "Login credentials incorrect. Try again.")


def welcome_page():
    global welcome_pg
    # Create the main window
    welcome_pg = tk.Tk()
    welcome_pg.geometry("800x770")
    welcome_pg.title("Welcome page")
    welcome_pg.configure(bg='#c3e5f6')

    # Create a label for the title
    welcome_title = tk.Label(welcome_pg, text=" Game: Pit and Peak of the Day ",
                     font=("Helvetica", 24), bg="white", borderwidth=3, relief="solid")
    welcome_title.pack(pady=5)

    # Create a label to display today's date
    date_label = tk.Label(welcome_pg, text=" Today's date: " + date.strftime("%B %d, %Y")+" ",
                          font=("Helvetica", 14), bg="white", borderwidth=3, relief="solid")
    date_label.pack(pady=5)

    # Create a button
    enter_button = tk.Button(welcome_pg, text="Enter", font=("Helvetica", 16),
                             bg="white", command=pit_page)
    enter_button.pack(pady=5)

    # Load the image
    image = Image.open('mtn_img.png')

    # Resize the image in the given (width, height)
    img = image.resize((800, 650))

    # Convert the image in TkImage
    my_img = ImageTk.PhotoImage(img)

    # Display the image with label
    welcome_label = tk.Label(welcome_pg, image=my_img)
    welcome_label.pack(pady=10)

    welcome_pg.mainloop()


def pit_page():
    welcome_pg.destroy()
    global pit_pg
    pit_pg = tk.Tk()
    pit_pg.geometry("600x770")
    pit_pg.title("Game: Pit Page")
    pit_pg.configure(bg='#E0E0E0')

    # Load the image
    pit_image = Image.open('pit.png')

    # Resize the image in the given (width, height)
    pit_img = pit_image.resize((325, 275))

    # Conver the image in TkImage
    pittk_img = ImageTk.PhotoImage(pit_img)

    # Display the image with label
    pitlabel = tk.Label(pit_pg, image=pittk_img, borderwidth=3, relief="solid", bg="white")
    pitlabel.image = pittk_img  # keep a reference!
    pitlabel.pack(pady=30)

    # Create a label for the title
    pit_title = tk.Label(pit_pg, text="Pit: What was the most challenging part of your day?",
                         font=("Helvetica", 24), bg="white", borderwidth=3, relief="solid")
    pit_title.pack(pady=5)

    # Create a text box for user input
    global pit_text
    pit_text = tk.Text(pit_pg, height=15, width=60, borderwidth=2, relief="solid")
    pit_text.pack(pady=5)

    # Create a submit button
    next_button = tk.Button(pit_pg, text="Next", font=("Helvetica", 16),
                            command= save_pit_data)
    next_button.pack(pady=5)

    pit_pg.mainloop()


def save_pit_data():
    global pit_text_content
    pit_text_content = pit_text.get("1.0", 'end-1c')
    print("Pit text: "+pit_text_content)
    pit_pg.destroy()
    peak_page()


def peak_page():
    global peak_pg, pittk_img, peak_label
    peak_pg = tk.Tk()
    peak_pg.geometry("600x770")
    peak_pg.title("Game: Peak Page")
    peak_pg.configure(bg='#E0E0E0')

    # Load the image
    peak_image = Image.open('peak.png')

    # Resize the image in the given (width, height)
    peak_img = peak_image.resize((325, 275))

    # Conver the image in TkImage
    peaktk_img = ImageTk.PhotoImage(peak_img)

    # Display the image with label
    peak_label = tk.Label(peak_pg, image=peaktk_img, borderwidth=3, relief="solid", bg="white")
    peak_label.image = peaktk_img  # keep a reference!
    peak_label.pack(pady=30)

    # Create a label for the title
    peak_title = tk.Label(peak_pg, text="Peak: What was the best part of your day?",
                          font=("Helvetica", 24), bg="white", borderwidth=3, relief="solid")
    peak_title.pack(pady=5)

    # Create a text box for user input
    global peak_text
    peak_text = tk.Text(peak_pg, height=15, width=60, borderwidth=2, relief="solid")
    peak_text.pack(pady=5)

    # Create a submit button
    submit_button = tk.Button(peak_pg, text="Submit", font=("Helvetica", 16),
                              command= save_peak_data)
    submit_button.pack(pady=5)

    peak_pg.mainloop()


def save_peak_data():
    global peak_text_content, time
    now = datetime.now()
    time = now.strftime("%H:%M:%S")
    peak_text_content = peak_text.get("1.0", 'end-1c')
    print("Peak text: "+peak_text_content)

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

    peak_pg.destroy()

    thank_you_page = tk.Tk()
    thank_you_page.geometry("1200x770")
    thank_you_page.title("Thank You Page")
    thank_you_page.configure(bg='#c3e5f6')

    # Create a label for the title
    thank_you_title = tk.Label(thank_you_page, text=" Thank you for your feedback! ",
                               font=("Helvetica", 24), bg="white", borderwidth=3, relief="solid")
    thank_you_title.pack(pady=5)

    quote_of_day_title = tk.Label(thank_you_page, text=" Quote of the day: ",
                               font=("Helvetica", 24), bg="white", borderwidth=3, relief="solid")
    quote_of_day_title.pack(pady=5)

    rand_num = random.randint(1,11)
    rand_str = str(rand_num)

    query2 = "select quote from quotes where quoteID = '%s'" % rand_str
    cursor.execute(query2)
    quote = cursor.fetchone()
    quote = str(quote)
    print_quote = str(quote[2:])
    print_quote = print_quote[:-3]
    print(print_quote)
    quote_title = tk.Label(thank_you_page, text=print_quote, font=("Helvetica", 24),
                           bg="white", borderwidth=3, relief="solid")
    quote_title.pack(pady=5)

    # Load the image
    image = Image.open('mtn_img.png')

    # Resize the image in the given (width, height)
    img = image.resize((800, 650))

    # Convert the image in TkImage
    my_img = ImageTk.PhotoImage(img)

    # Display the image with label
    label = tk.Label(thank_you_page, image=my_img, borderwidth=3, relief="solid")
    label.pack(pady=10)

    cursor.close()

    thank_you_page.mainloop()


# Create the main window
app = tk.Tk()
app.title("Cyber Devils Login Page")
app.geometry("573x731")

# Add the background image
back_image = tk.PhotoImage(file="Journal.png")
back_label = tk.Label(app, image=back_image)
back_label.pack(fill="both", expand=True)

intro = tk.Label(app, text="\n\nWELCOME \nPlease login to your account:\n ",
                 font='Times 14 bold', bg="black", fg="white")
intro.place(x=170, y=235)

tries = 0

# Username Input
userrow = tk.Label(app, text="Username:", bg="black", fg="white")
userrow.place(x=150, y=360)
userrow_entry = tk.Entry(app, width=25)
userrow_entry.place(x=250, y=360)

# Password Input
passrow = tk.Label(app, text="Password:", bg="black", fg='white')
passrow.place(x=150, y=400)
passrow_entry = tk.Entry(app, show="*", width=25)
passrow_entry.place(x=250, y=400)

# Login Button
submitbtn = tk.Button(app, text="Login", bg='green', fg='black', command=login)
submitbtn.place(x=270, y=450)

# Start the main event loop
app.mainloop()

# login test credential
# sauer.price
# afcf97aeaa2acfbc9c9f856bcc53744a