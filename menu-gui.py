import tkinter as tk

# Create a Tkinter root window
root = tk.Tk()

# Set the size of the window
root.geometry("330x400")

# Set the title of the window
root.title("Restaurant Order System")

# Create a label at the top of the window
label = tk.Label(root, text="MENU", font=("Arial", 15), bg="#90EE90")
label.pack(side="top", fill="x", pady=10)


# Create a frame for the spin boxes
spin_box_frame = tk.Frame(root)
spin_box_frame.pack(side="top", pady=10)

# Create three labels and spin boxes for the items
cookie_label = tk.Label(spin_box_frame, text="Cookie", anchor="w")
cookie_spin_box = tk.Spinbox(spin_box_frame, from_=0, to=10, width=5)
cookie_label.grid(row=0, column=0, padx=(40, 10), pady=5)
cookie_spin_box.grid(row=0, column=1, padx=(0, 40), pady=5)

sandwich_label = tk.Label(spin_box_frame, text="Sandwich", anchor="w")
sandwich_spin_box = tk.Spinbox(spin_box_frame, from_=0, to=10, width=5)
sandwich_label.grid(row=1, column=0, padx=(40, 10), pady=5)
sandwich_spin_box.grid(row=1, column=1, padx=(0, 40), pady=5)

drink_label = tk.Label(spin_box_frame, text="Drink", anchor="w")
drink_spin_box = tk.Spinbox(spin_box_frame, from_=0, to=10, width=5)
drink_label.grid(row=2, column=0, padx=(40, 10), pady=5)
drink_spin_box.grid(row=2, column=1, padx=(0, 40), pady=5)

# Create a frame for the buttons
button_frame = tk.Frame(root)
button_frame.pack(side="top", pady=10)

# Create a submit button
submit_button = tk.Button(button_frame, text="Submit", width=10)
submit_button.pack(side="left", padx=(60, 5))

# Create a clear button
clear_button = tk.Button(button_frame, text="Clear", width=10)
clear_button.pack(side="left", padx=(5, 60))

# Create a text box to print out the itemized list and grand total
text_box = tk.Text(root, width=30, height=10)
text_box.pack(side="top", fill="x", pady=10)


# Define the main function
def main():
    # Get the number of cookies, sandwiches, and drinks
    cookies = int(cookie_spin_box.get())
    sandwiches = int(sandwich_spin_box.get())
    drinks = int(drink_spin_box.get())

    # Create a dictionary with item names as keys and their respective prices as values
    items = {"cookie": (cookies, 1.50), "sandwich": (sandwiches, 4.00), "drink": (drinks, 1.00)}

    # Calculate the total cost and initialize the total variable
    total = 0
    output = ""
    output += "---------------------------\n"
    for item, values in items.items():
        if values[0] > 0:
            output += "(%d) - %s = $%.2f\n" % (values[0], item.capitalize(), values[0] * values[1])
            total += values[0] * values[1]
    output += "---------------------------\n"
    output += "GRAND TOTAL = $%.2f\n" % total
    output += "---------------------------\n"

    # Clear the text box
    text_box.delete(1.0, tk.END)
    # Insert the output into the text box
    text_box.insert(tk.END, output)


def clear_cart():
    # Clear the spin boxes
    cookie_spin_box.delete(0, tk.END)
    cookie_spin_box.insert(tk.END, "0")
    sandwich_spin_box.delete(0, tk.END)
    sandwich_spin_box.insert(tk.END, "0")
    drink_spin_box.delete(0, tk.END)
    drink_spin_box.insert(tk.END, "0")

    # Clear the text box
    text_box.delete(1.0, tk.END)


# Connect the submit button to the main() function
submit_button.config(command=main)

# Connect the clear button to the clear_cart() function
clear_button.config(command=clear_cart)

# Make the window non-resizable
root.resizable(width=False, height=False)

# Show the window
root.mainloop()
