from tkinter import *
from Exercise1 import exercise1
from Exercise2 import exer2

root_main = Tk()
#root_main.iconphoto(False, PhotoImage(file='D:\\Python projects\\MISC\\icon.png'))
root_main.configure(bg="white")
root_main.geometry("350x150")
root_main.resizable(False, False)
root_main.title("Stowage Calculator")

main_name = Label(root_main, text="Stowage Calculator", font='Helvetica 15 bold', bg="white")
main_name.grid(row=0, column=0,padx=85)

ex1 = Button(root_main, text="Exercise 1", bg="white", width=8, height=2, command= exercise1)
ex1.place(x=15, y=31)
ex2 = Button(root_main, text="Exercise 2", bg="white", width=8, height=2, command= exer2)
ex2.place(x=100, y=31)



root_main.mainloop()