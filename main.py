
import tkinter as tk

def convert_units():
    input_value = entry.get()
    output_value = round(float(input_value) * 1.60934, 4)
    label4.config(text=f'{output_value}')

window = tk.Tk()
window.title("Unit Converter")
window.minsize(350, 150)
window.config(padx=50, pady=50)

label1 = tk.Label(window, text="is equal to", font=("Arial", 18, 'normal'))
label1.grid(row=1, column=0)

label2 = tk.Label(window, text="Miles", font=("Arial", 18, 'normal'))
label2.grid(row=0, column=2)

label3 = tk.Label(window, text="Kilometers", font=("Arial", 18, 'normal'))
label3.grid(row=1, column=2)

label4 = tk.Label(window, text=0, font=("Arial", 18, 'normal'))
label4.grid(row=1, column=1)

entry = tk.Entry(width=10)
entry.config(font=("Arial", 18, 'normal'))
entry.grid(row=0, column=1)

button = tk.Button(text="Calculate", font=("Arial", 18, 'normal'), command=convert_units)
button.grid(row=2, column=1)

window.mainloop()