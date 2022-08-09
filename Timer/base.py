import tkinter as tk
from tkinter import *
import os
import time
from tkinter import messagebox
import winsound

def start_timer():
    try:
        int(entry_wtime.get())
        int(entry_rtime.get())
        int(entry_repetitions.get())
        while int(entry_repetitions.get()) > 0:
            time.sleep(int(entry_wtime.get()))
            winsound.Beep(500, 600)

            time.sleep(int(entry_rtime.get()))
            winsound.Beep(1000,600)
            state = int(entry_repetitions.get())-1
            entry_repetitions.delete(0, END)
            entry_repetitions.insert(0, state)  
            
        else:
           tk.messagebox.showinfo("Workout Timer", "Bien Hecho! vales gato")

    except:
        tk.messagebox.showwarning("Workout Timer", "pon un numero ya piensa")

root = tk.Tk()
root.title("Workout Timer")
root.geometry("400x400")

entry_wtime = Entry(root, width=30, bg="black", fg="white", borderwidth=5, text="workout")
entry_wtime.pack(pady=20, padx=10)
entry_rtime = Entry(root, width=30, bg="black", fg="white", borderwidth=5, text="rest")
entry_rtime.pack(pady=20, padx=10)
entry_repetitions =  Entry(root, width=30, bg="black", fg="white", borderwidth=5, text="Repetitions")
entry_repetitions.pack(pady=20, padx=10)

button_start = tk.Button(root, text="Start Workout", padx=20, pady=20, fg="white", bg="black", command=start_timer)
button_start.pack(pady=20, padx=10)


root.mainloop()