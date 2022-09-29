import random
import tkinter as tk
from tkinter.ttk import LabelFrame
import random

def random_number():
    num =random.randint(1,25)
    r_num.config(text = num)

style= tk.Tk()
style.geometry("600x600")
style.config(bg="#2e9fb3")
#style.resizable(width=False,height=False)
style.title('Random  Number Generator-BINGO')
text= tk.Label(text="Random Number Generator",font=("Arial",80),bg="#2e9fb3")
button = tk.Button(text="Click  me for a  number",font=("Arial",40),bg="#A3E4D7",command=random_number)
r_num = tk.Label(bg="#2e9fb3",font=("Arial",100),text="")

text.place(x=180,y=40)
button.place(x=510,y=270)
r_num.place(x=650,y=430)


style.mainloop()
