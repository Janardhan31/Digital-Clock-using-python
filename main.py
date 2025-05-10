import tkinter as tk       #module for making gui
from time import strftime      #module for current time and date

root = tk.Tk()
root.title("digital clock")

def time():
    string = strftime('%H:%M:%S %p \n %x')  # Corrected format string
    label.config(text=string)
    label.after(1000, time)  # Update the time every second

label = tk.Label(root, font=('calibri', 40, 'bold'), background='black', foreground='white')
label.pack(anchor='center')  #anchor the label to the center of the window
time()  #call the time function to update the time

root.mainloop()  #run the main loop to keep the window open