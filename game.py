import tkinter as tk
from tkinter import messagebox
import random

# Function to determine winner
def determine_winner(user_choice):
    choices = ['Rock', 'Paper', 'Scissors']
    comp_choice = random.choice(choices)

    result = ""

    if user_choice == comp_choice:
        result = "It's a tie!"
    elif (user_choice == 'Rock' and comp_choice == 'Scissors') or \
         (user_choice == 'Paper' and comp_choice == 'Rock') or \
         (user_choice == 'Scissors' and comp_choice == 'Paper'):
        result = "You win!"
    else:
        result = "Computer wins!"

    result_label.config(text=f"Computer chooses: {comp_choice}\nResult: {result}")

# Initialize Tkinter
root = tk.Tk()
root.title("Rock, Paper, Scissors Game")

# Function to handle button clicks
def on_button_click(choice):
    determine_winner(choice)

# Buttons
rock_button = tk.Button(root, text="Rock", command=lambda: on_button_click("Rock"))
rock_button.grid(row=0, column=0, padx=5, pady=5)

paper_button = tk.Button(root, text="Paper", command=lambda: on_button_click("Paper"))
paper_button.grid(row=0, column=1, padx=5, pady=5)

scissors_button = tk.Button(root, text="Scissors", command=lambda: on_button_click("Scissors"))
scissors_button.grid(row=0, column=2, padx=5, pady=5)

# Result label
result_label = tk.Label(root, text="")
result_label.grid(row=1, column=0, columnspan=3, padx=5, pady=5)

# Start the GUI
root.mainloop()
