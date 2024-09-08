import tkinter as tk
import random
import pyperclip

def generate_password():
    lower = 'abcdefghijklmnopqrstuvwxyz'
    upper = 'ABCDEFGHIJKLMNOPQRST'
    symbol = '(){}[];#*._'
    all_chars = lower + upper + symbol
    length = int(length_entry.get())
    
    password = ''.join(random.sample(all_chars, length))
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)
    pyperclip.copy(password)

# Create the main Tkinter window
root = tk.Tk()
root.title("Password Generator")

# Create and configure widgets
length_label = tk.Label(root, text="Length of Password:")
length_entry = tk.Entry(root, width=5)
generate_button = tk.Button(root, text="Generate Password", command=generate_password)
password_label = tk.Label(root, text="Generated Password:")
password_entry = tk.Entry(root, width=20)

# Place widgets in the window
length_label.grid(row=0, column=0, pady=10)
length_entry.grid(row=0, column=1, pady=10)
generate_button.grid(row=1, column=0, columnspan=2, pady=10)
password_label.grid(row=2, column=0, pady=10)
password_entry.grid(row=2, column=1, pady=10)

# Run the Tkinter event loop
root.mainloop()


print()
print()