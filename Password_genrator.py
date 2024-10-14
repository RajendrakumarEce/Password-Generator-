import tkinter as tk
from tkinter import ttk
import random
import string

def generate_password():
    length = int(length_var.get())
    use_lower = lowercase_var.get()
    use_upper = uppercase_var.get()
    use_digits = digits_var.get()
    use_special = special_var.get()

    characters = ""
    if use_lower:
        characters += string.ascii_lowercase
    if use_upper:
        characters += string.ascii_uppercase
    if use_digits:
        characters += string.digits
    if use_special:
        characters += string.punctuation

    if not characters:
        result_var.set("Please select at least one character type.")
        return

    password = ''.join(random.choice(characters) for _ in range(length))
    result_var.set(password)

# Create the main window
root = tk.Tk()
root.title("Password Generator")
root.geometry("400x350")
root.resizable(False, False)

# Custom color scheme
bg_color = "#2C3E50"  # Dark blue-gray
fg_color = "#ECF0F1"  # Light gray
accent_color = "#3498DB"  # Bright blue
button_color = "#2980B9"  # Darker blue

root.configure(bg=bg_color)

# Style
style = ttk.Style()
style.theme_use('clam')
style.configure('TFrame', background=bg_color)
style.configure('TLabel', background=bg_color, foreground=fg_color)
style.configure('TCheckbutton', background=bg_color, foreground=fg_color)
style.configure('TButton', background=button_color, foreground=fg_color)
style.map('TButton', background=[('active', accent_color)])
style.configure('TEntry', fieldbackground=fg_color, foreground=bg_color)

# Variables
length_var = tk.StringVar(value="12")
lowercase_var = tk.BooleanVar(value=True)
uppercase_var = tk.BooleanVar(value=True)
digits_var = tk.BooleanVar(value=True)
special_var = tk.BooleanVar(value=True)
result_var = tk.StringVar()

# Frames
input_frame = ttk.Frame(root, padding="10")
input_frame.pack(fill="x", padx=20, pady=10)

options_frame = ttk.Frame(root, padding="10")
options_frame.pack(fill="x", padx=20, pady=10)

result_frame = ttk.Frame(root, padding="10")
result_frame.pack(fill="x", padx=20, pady=10)

# Length input
ttk.Label(input_frame, text="Password Length:").pack(side="left")
length_entry = ttk.Entry(input_frame, textvariable=length_var, width=5)
length_entry.pack(side="left", padx=5)

# Character type options
ttk.Checkbutton(options_frame, text="Lowercase", variable=lowercase_var).pack(anchor="w")
ttk.Checkbutton(options_frame, text="Uppercase", variable=uppercase_var).pack(anchor="w")
ttk.Checkbutton(options_frame, text="Digits", variable=digits_var).pack(anchor="w")
ttk.Checkbutton(options_frame, text="Special Characters", variable=special_var).pack(anchor="w")

# Generate button
generate_button = ttk.Button(root, text="Generate Password", command=generate_password)
generate_button.pack(pady=10)

# Result display
result_entry = ttk.Entry(result_frame, textvariable=result_var, state="readonly", width=30)
result_entry.pack(side="left", padx=5)

# Copy button
def copy_to_clipboard():
    root.clipboard_clear()
    root.clipboard_append(result_var.get())
    root.update()

copy_button = ttk.Button(result_frame, text="Copy", command=copy_to_clipboard)
copy_button.pack(side="left")

# Title
title_label = ttk.Label(root, text="Password Generator", font=("Helvetica", 16, "bold"))
title_label.pack(pady=10)

root.mainloop()