from tkinter import *
from tkinter import messagebox
from random import choice

#Fkt zu Messageboxactionen
def info_box():
    infotxt = "***********************\nAutor: Kevin Rettig\nDatum: 22.12.2017\nVersion: 1.2.0\n***********************"
    messagebox.showinfo(message = infotxt, title = "Info")


def datei_exit():
    fenster.destroy()

def beschreibung_menu():
    beschreibung = "Dieser Buchstabengenerator erzeugt zufällige Buchstaben des gesamten Alphabetes, für zum Beispiel das Spiel Stadt-Land-Fluss. Wenn alle Buchstaben verwendet wurden muss die Taste \'Neues Spiel\' verwendet werden. Untypische Buchstaben wie X, Y, Z oder auch Umlaute sind über den Button \'Spaßrunde\' zu erreichen. Alle bereits verwendeten Buchstaben werden im Fenster angezeigt, in der Reihenfolge in welcher sie auftraten. \n Viel Spaß beim spielen! "
    messagebox.showinfo(message = beschreibung, title = 'Beschreibung')

#Fenster erstellen
fenster = Tk()
fenster.geometry("800x600")
fenster.title("Zufallsbuchstabe")
fenster.iconbitmap('IcoZilla.ico')

#Menüleiste erstellen
menueleiste = Menu(fenster)
dateimenue=Menu(menueleiste, tearoff=0)
infomenue = Menu(menueleiste, tearoff=0)
beschreibung = Menu(menueleiste, tearoff=0)
dateimenue.add_command(label="Exit", command=datei_exit)
infomenue.add_command(label="Info", command=info_box)
infomenue.add_command(label="Beschreibung", command=beschreibung_menu)
menueleiste.add_cascade(label="Datei", menu=dateimenue)
menueleiste.add_cascade(label="Info", menu=infomenue)

#Def+Fkt für Programm
alphabet = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","R","S","T","U","V","W"]
funny = ["X","Y","Z","Ä","Ö","Ü","Q"]
played = []
played_funny = []

def generate():
    Z = choice(alphabet)
    alphabet.remove(Z)

    buchstaben_label.config(text="Der Buchstabe lautet: \n" + Z)
    played.append(Z)
    played_label.config(text=played+played_funny)

def funnyround():
    f = choice(funny)
    funny.remove(f)

    buchstaben_label.config(text="Der Buchstabe lautet: \n" + f)
    played_funny.append(f)
    played_label.config(text=played+played_funny)

def beenden():
    fenster.destroy()

def newgame():
    alphabet.extend(played)
    funny.extend(played_funny)
    del played[:]
    del played_funny[:]
    played_label.config(text="Schon gespielt: ")
    buchstaben_label.config(text="Der Buchstabe lautet:\n ")

#Button und Label erstellen und positionieren
exit_button = Button(fenster, text="Beenden", command=beenden)
generate_button = Button(fenster, text="Buchstabe \ngenerieren", command=generate)
newgame_button = Button(fenster, text="Neues Spiel", command=newgame)
funny_button = Button(fenster, text="Spaßrunde", command=funnyround)

info_label = Label(fenster, text="Zum generieren eines \n Buchstaben, Button klicken")
buchstaben_label = Label(fenster, text="Der Buchstabe lautet:\n ", fg="red", font="Helvetica 12")
played_label = Label(fenster, text="Schon gespielt: ")
funny_label = Label(fenster, text="Für eine Spaßrunde,\n den Funnybutton klicken!")

generate_button.place(x=80, y=110, width=200, height=150)
info_label.place(x=50, y=30, width=250, height=75)
buchstaben_label.place(x=450, y=80, width=250, height=75)
exit_button.place(x=600, y=350, width=150, height=50)
played_label.place(x=50, y=450, width=700, height=75)
newgame_button.place(x=400, y=220, width=150, height=50)
funny_button.place(x=400, y=300, width=150, height=100)
funny_label.place(x=50, y=300, width=250, height=75)

#Menü einbinden und Fenster abschließen
fenster.config(menu=menueleiste)
fenster.mainloop()
