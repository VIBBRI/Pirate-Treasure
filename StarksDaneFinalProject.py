# Importing necessary modules
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk


# Modular Approach
class App:

    # Initializes the App with a given tkinter root
    def __init__(self, root): 
        self.root = root  # tkinter root window
        self.create_main_window()  # Call the method to create the main window

    # Method to create the main window
    def create_main_window(self): 
        # Clear window - Remove all existing widgets from the root window
        for widget in self.root.winfo_children():
            widget.destroy()

        # Set the title for the main window
        self.root.title("My chance at riches!")

        # Load and display the first image
        img = Image.open("image1.jpg")  # Open the image using PIL
        photo = ImageTk.PhotoImage(img)  # Convert the image to PhotoImage type
        label1 = tk.Label(self.root, text="Old Door", image=photo)  # Create a label widget to display the image with alternate text
        label1.image = photo  # Reference to the image object (to avoid garbage collection)
        label1.pack(pady=10)  # Place the label on the window with some padding

        # Display text below the image
        label3 = tk.Label(self.root, text=f"Aaarrr, you want my treasures? You'll have to guess me password first. It might take days, weeks, YEARS, EVEN!")
        label3.pack(pady=10)

        # Create an entry box for user input
        self.user_entry = tk.Entry(self.root)  # Entry widget for password input
        self.user_entry.pack(pady=10)

        # Button to navigate to the second window
        btn1 = tk.Button(self.root, text="Enter Password", command=self.navigate_to_second)
        btn1.pack(pady=10)

        # Button to show a hint message
        btn2 = tk.Button(self.root, text="What's the password?", command=self.display_message)
        btn2.pack(pady=10)

        # Button to exit the application
        btn3 = tk.Button(self.root, text="Whatever, I'm out.", command=self.safe_exit)
        btn3.pack(pady=10)

    # Method to create the second window, which is shown after the password is entered
    def create_second_window(self, user_input):
        # Clear window - Remove all existing widgets
        for widget in self.root.winfo_children():
            widget.destroy()

        # Set the title for the second window
        self.root.title("......Hooray?")

        # Load and display the second image
        img = Image.open("image2.jpg")
        photo = ImageTk.PhotoImage(img)
        label2 = tk.Label(self.root, text="Toy treasure chest for Halloween", image=photo)
        label2.image = photo
        label2.pack(pady=10)

        # Display a message that includes the user's input
        label3 = tk.Label(self.root, text=f"Oh yeah, I'm sure '{user_input}' was it. Here ye go, I have too much of this stuff, anyway.")
        label3.pack(pady=10)

        # Button to return to the main window
        btn = tk.Button(self.root, text="I want more!", command=self.create_main_window)
        btn.pack(pady=10)

    # Method to navigate to the second window when the "Enter Password" button is clicked
    def navigate_to_second(self):
        user_input = self.user_entry.get()  # Get the text from the entry widget
        if not user_input:  # Check if the entry is empty
            messagebox.showerror("What?", "You haven't even said anything!")  # Show error message if empty
            return
        self.create_second_window(user_input)  # If not empty, go to the second window

    # Method to show a hint message when the "What's the password?" button is clicked
    def display_message(self):
        messagebox.showinfo("Well...", "Can't say I remember it. I'll know it when I hear it, though.")

    # Method to safely close the application when the "Exit" button is clicked
    def safe_exit(self):
        self.root.destroy()


# Main: Entry point of the program
if __name__ == "__main__":
    root = tk.Tk()  # Create the root tkinter window
    app = App(root)  # Create an instance of the App class
    root.mainloop()  # Start the tkinter main loop
