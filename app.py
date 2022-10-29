import tkinter as tk
from tkinter import ttk

from passgen import generate_pwd

root = tk.Tk() # initialize tk
root.title('Password Generator') # set window title
root.geometry('300x200') # set window width and height
root.resizable(False, False)

frame = ttk.Frame(root)

length_var = tk.IntVar(value=6) # default password length
digit_var = tk.BooleanVar() # include digit
special_var = tk.BooleanVar() # include special character
entry_var = tk.StringVar()

# Entry widget
entry = tk.Entry(frame, textvariable=entry_var)
entry.pack(fill='x', padx=20)

# Slider label widgets
slider_label = ttk.Label(frame, text='Character Length')
slider_label.pack()

slider_value = ttk.Label(frame, text=length_var.get())
slider_value.pack()
# Slider widget
slider = ttk.Scale(
    frame, 
    from_=8, 
    to=32, 
    orient='horizontal', 
    variable=length_var, 
    command=lambda e: slider_value.configure(text=length_var.get())
)
slider.pack(fill='x', padx=20)

# Include numbers checkbox
digit_checkbox = ttk.Checkbutton(frame, text='Include digits', onvalue=True, offvalue=False, variable=digit_var)
digit_checkbox.pack(fill='x', padx=20)

# Include special characters checkbox
special_checkbox = ttk.Checkbutton(frame, text='Include special characters', onvalue=True, offvalue=False, variable=special_var)
special_checkbox.pack(fill='x', padx=20)

def on_generate():
    # Get checkbox values
    is_digit = digit_var.get()
    is_special = special_var.get()
    length = length_var.get()

    password = generate_pwd(length, is_digit, is_special) # generate password
    entry_var.set(password) # display password with entry widget

# Generate password
button = ttk.Button(frame, text='Generate', command=on_generate)
button.pack(pady=20)

frame.pack(fill='x', expand=True)
# application loop
root.mainloop()