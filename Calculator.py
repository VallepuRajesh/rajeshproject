import tkinter as tk

 

 

# Function to handle button clicks

def click(event):

    text = event.widget.cget("text")

    if text == "=":

        try:

            expression = screen.get()

            # Replace 'x' with '*' for proper evaluation

            expression = expression.replace("x", "*")

            expression = expression.replace("%", "/100")

            result = str(eval(expression))

            screen.set(result)

        except Exception as e:

            screen.set("Error")

    elif text == "C":

        screen.set("")

    elif text == "⌫":  # Backspace button

        current_text = screen.get()

        screen.set(current_text[:-1])  # Remove the last character

    else:

        screen.set(screen.get() + text)

 

 

# Create a GUI window

root = tk.Tk()

root.geometry("400x600")

root.title("Calculator")

 

# Create a StringVar to display the input and result

screen = tk.StringVar()

entry = tk.Entry(

    root, textvar=screen, font=("Helvetica", 36), justify="right", bd=15, insertwidth=4

)

entry.pack(fill=tk.BOTH, ipadx=8, padx=10, pady=10, expand=True)

 

# Create a frame for buttons

button_frame = tk.Frame(root)

button_frame.pack()

 

# Button text

button_text = [

    ("7", 1, 0),

    ("8", 1, 1),

    ("9", 1, 2),

    ("/", 1, 3),

    ("4", 2, 0),

    ("5", 2, 1),

    ("6", 2, 2),

    ("x", 2, 3),  # Use 'x' for multiplication

    ("1", 3, 0),

    ("2", 3, 1),

    ("3", 3, 2),

    ("-", 3, 3),

    ("0", 4, 0),

    (".", 4, 1),

    ("C", 4, 2),

    ("+", 4, 3),

    ("=", 5, 0),

    ("%", 5, 1),  # Add the '%' button

    ("⌫", 5, 2),  # Backspace button

]

 

# Create buttons and add click event

for btn_text, i, j in button_text:

    btn = tk.Button(

        button_frame, text=btn_text, font=("Helvetica", 18), padx=20, pady=20

    )

    btn.grid(row=i, column=j, padx=5, pady=5, sticky="nsew")

    btn.bind("<Button-1>", click)

 

# Configure grid weights to make buttons expand uniformly

for i in range(6):

    button_frame.grid_rowconfigure(i, weight=1)

for j in range(4):

    button_frame.grid_columnconfigure(j, weight=1)

 

# Start the GUI main loop

root.mainloop()