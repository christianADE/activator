import tkinter as tk
from tkinter import *
from tkinter import messagebox

import subprocess

import os


#fenetre de l'app

fen = tk.Tk()
fen.geometry("500x350")
fen.title("Activator")
fen.configure(bg= "#fadb61")
fen.resizable(False, False)


def powershell_as_admin():
    code = "iex(irm https://get.activated.win)"
    powershell_command = f"powershell -Command Start-Process powershell -ArgumentList '-Command \"{code}\"' -Verb RunAs"
    subprocess.run(powershell_command, shell=True)

def redemarrage():
    command = "shutdown /r"
    subprocess.run(command, shell=True)

Lbl = tk.Label(text="Bienvenue dans l'activateur de windows et office", bg= "#fadb61", font= 16)
Lbl.place(x= 80, y= 60)

bouton = tk.Button(fen, text= "Activer", bg= "blue", fg= "white", font=('Times new romain', 20), command=powershell_as_admin)
bouton.place(x=100, y= 150)

bout = tk.Button(fen, text= "Redemarrer", bg= "red", fg= "white", font=('Times new romain', 20), command= redemarrage)
bout.place(x=230, y= 150)


fen.mainloop()

