import tkinter as tk
from tkinter import PhotoImage
from tkinter import Text
from datetime import date

# Get today's date
today = date.today()

def store_pit_text(pittext, peaktext):
    global pit_text_content, peak_text_content
    pit_text_content = pittext.get("1.0", 'end-1c')
    print("Pit text: "+pit_text_content)
    peak_text_content = peaktext.get("1.0", 'end-1c')
    print("Peak text: "+peak_text_content)

    pitnpeak_page.destroy()
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


def go_to_pit_page():
    root.destroy()
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
root = tk.Tk()
root.geometry("800x770")
root.title("Welcome page")

# Create a label for the title
title = tk.Label(root, text="Game: Pit and Peak of the Day", font=("Helvetica", 24))
title.pack(pady=5)

# Create a label to display today's date
date_label = tk.Label(root, text="Today's date: " + today.strftime("%B %d, %Y"), font=("Helvetica", 14))
date_label.pack(pady=5)

# Create a button
enter_button = tk.Button(root, text="Enter", font=("Helvetica", 16), command=go_to_pit_page)
enter_button.pack(pady=5)

# Create a PhotoImage object for the background image
image = PhotoImage(file="mountain.png")

# Create a label to hold the image
background_label = tk.Label(root, image=image)
background_label.pack(fill="both", expand=True)

# Start the main event loop
root.mainloop()
