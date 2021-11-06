from tkinter import *
import random

root = Tk()
root.title("mexico")
root.geometry("500x500")
length = 7
randomint = 0
info = Label(root,text="")
letter=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","yene","eney"]
def start():
    i=0
    name=""
    while i<length:
        randomint = random.randint(0,27)
        name = name+letter[randomint]
        i+=1
    print(name)
    info["text"] = name
btn = Button(root,text="press",command=start)
btn.place(rely = 0.5,relx=0.5)
info.place(rely = 0.6,relx=0.5)
root.mainloop()