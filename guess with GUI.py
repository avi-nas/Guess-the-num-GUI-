import random
from tkinter import *
import math

limit = random.randint(40,300)
answer = random.randint(1,limit)
attempts = int(math.log2(limit))
def check_answer():
    global attempts
    global text
    attempts -= 1
    guess = int(entry_window.get())
    if answer == guess:
        text.set("You won")
        btn_check.pack_forget()
    elif(attempts==0):
        text.set(" NO attempts left")
        btn_check.pack_forget()
    elif guess < answer:
        text.set("Incorrect!! You have"+ str(attempts) + "attempts left --go higher")
    elif guess > answer:
        text.set("Incorrect!! You have" + str(attempts) + "attempts left --go lower")
    return
root = Tk()
root.title("Guess The Number")
root.geometry("400x200")
root.maxsize("500","300")
root.minsize('400','200')
label = Label(root, text=f"Guess a number between 1 to {limit}")
label.pack()
entry_window = Entry(root,width=40, borderwidth=4)
entry_window.pack()
btn_check = Button(root, text="check", command=check_answer)
btn_check.pack()
btn_quit =Button(root, text="quit",  command=root.destroy)
btn_quit.pack()
text = StringVar()
text.set(f"You have {attempts} attmempts")
guess_attempts= Label(root, textvariable=text)
guess_attempts.pack()
root.mainloop()