import tkinter as tk
import random

#we're setting number to choose a number between 1 & 100
number = random.randint(1, 100)

#define get response so you can input the number
def get_response(event=None):
    message = entry.get()
    try:
        guess = int(message)
    except:
        conversation.insert(tk.END, f"You: {message}\n")
        conversation.insert(tk.END, f"Bot: Please enter a number\n")
        entry.delete(0, tk.END)
        conversation.see(tk.END)
        return

    conversation.insert(tk.END, f"You: {guess}\n")
    if guess == number:
        conversation.insert(tk.END, f"Bot: Correct! The number was {number}\n")
    elif guess < number:
        conversation.insert(tk.END, f"Bot: The number is higher\n")
    else:
        conversation.insert(tk.END, f"Bot: The number is lower\n")

    entry.delete(0, tk.END)
    conversation.see(tk.END)

#setting up the GUI to display as a window
root = tk.Tk()
root.geometry("600x450")
root.title("Andy's Awesome Guess the Number Chatbot GUI")

conversation = tk.Text(root)
conversation.pack(expand=True, fill='both')

entry = tk.Entry(root)
entry.pack()

button = tk.Button(root, text="Guess", command=get_response)
button.pack()

root.bind('<Return>', get_response)

root.mainloop()
