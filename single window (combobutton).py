import tkinter as tk
from tkinter import *
import os
import time
from tkinter import messagebox
import winsound
from tkinter import ttk

def clear_screen():
    entry_worktime.pack_forget()
    entry_resttime.pack_forget()
    entry_repetitions.pack_forget()
    button_start.pack_forget()
    button_30_15.pack_forget()


def start_menu():
    screen.pack_forget()
    entry_worktime.pack(pady=20, padx=10)
    entry_resttime.pack(pady=20, padx=10)
    entry_repetitions.pack(pady=20, padx=10)
    button_start.pack(pady=20, padx=10)
    button_30_15.pack(pady=20, padx=10)
    
    
def runtimes(worktime, resttime, repetitions):
    if repetitions > 0:
        if worktime > 0:
            screen.config(text=worktime, bg="#a8dadc")
            screen.pack(expand=True)
            worktime = worktime-1
            screen.after(1000, lambda: runtimes(worktime, resttime, repetitions))

        else:
            screen.config(text=resttime, bg="#1d3557")
            screen.pack(expand=True)
            resttime = resttime-1
            screen.after(1000, lambda: runtimes(worktime, resttime, repetitions))
            if resttime > -1:
                pass

            else:
                repetitions = repetitions-1
                worktime = int(entry_worktime.get())
                resttime = int(entry_resttime.get())
                runtimes(worktime, resttime, repetitions)

    else:
        screen.config(text="Done", bg="#e63946")
        screen.after(2000, start_menu)


def start_timer():
    try:
        int(entry_worktime.get())
        int(entry_resttime.get())
        int(entry_repetitions.get())                 #check all entries
        global worktime
        worktime = int(entry_worktime.get())
        global resttime
        resttime = int(entry_resttime.get())
        global repetitions
        repetitions = int(entry_repetitions.get())  #set all times
        clear_screen()
        runtimes(worktime, resttime, repetitions)

    except:
        clear_screen()
        screen.config(text="Pon un número, ya piensa", bg="#e63946")
        screen.pack(expand=True)
        screen.after(2000, start_menu)

# def total_():
#     try:
#         total = int(entry_resttime.get())*int(entry_repetitions.get())+int(entry_worktime.get())*int(entry_repetitions.get())

#     except:
#         total = "0"

def set_profile(work, rest):
    entry_worktime.current(int(work/5))
    entry_resttime.current(int(rest/5)+1)
    entry_repetitions.current(10)


options_worktime = ["--enter workouttime--"]
options_resttime = ["--enter resttime--", 0]
options_repetitions = ["--enter repetitions--"]


for x in range(1,20):
    options_worktime.append(x*5)
    options_resttime.append(x*5)
    options_repetitions.append(x)



#define window (Root)
root = tk.Tk()
root.title("Workout Timer")
root.geometry("400x400")
root.configure(bg="#457b9d")

#format text
format_screen = ("Arial", "18", "bold")
format_labels = ("Arial", "10", "bold")
format_entry = ("Arial", "10")



#set up entrys 
entry_worktime = ttk.Combobox(root, value=options_worktime, font=format_entry)
entry_worktime.current(0)
#Entry(root, width=30, bg="#a8dadc", fg="black", borderwidth=5, text="workout")
entry_resttime =  ttk.Combobox(root, value=options_resttime, font=format_entry)
entry_resttime.current(0)
#Entry(root, width=30, bg="#1d3557", fg="white", borderwidth=5, text="rest")
entry_repetitions =  ttk.Combobox(root, value=options_repetitions, font=format_entry)
entry_repetitions.current(0)
#Entry(root, width=30, bg="green", fg="white", borderwidth=5, text="Repetitions")


#start button
button_start = tk.Button(root, text="Start Workout", padx=20, pady=20, fg="white", bg="black", command=start_timer, font=format_labels)

#total time label
# total_time = Label(root, text=total + "Seconds")

#profiles
button_30_15 = tk.Button(root, text="30-15", padx=20, pady=20, bg="#f1faee", command=lambda : set_profile(30, 15))

#set up info windows
screen = Label(root, text="", bg="#457b9d", height=400, width=400, font=format_screen)

#pack start menu
start_menu()
# entry_worktime.pack(pady=20, padx=10)
# entry_resttime.pack(pady=20, padx=10)
# entry_repetitions.pack(pady=20, padx=10)
# # total_time.pack(pady=20, padx=10)
# button_start.pack(pady=20, padx=10)
# button_30_15.pack(pady=20, padx=10)

root.mainloop()