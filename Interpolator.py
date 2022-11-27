from tkinter import *

def interwin():
    # .pack() puts the widget inside the main window
    # when we write () after a function it automatically calls it always so when we want to call a function on command we write it without ()

    # calls the main window widget
    window = Toplevel()

    # Labels
    Label_given_x = Label(window, text="Given Number (x)", bg="white", font='Helvetica 9 bold')
    Label_given_x.place(x=139, y=-5)
    Label_given_x1 = Label(window, text="x1", bg="white", font='Helvetica 10 bold')
    Label_given_x1.place(x=54, y=48)
    Label_given_x2 = Label(window, text="x2", bg="white", font='Helvetica 10 bold')
    Label_given_x2.place(x=54, y=98)
    Label_given_y1 = Label(window, text="y1", bg="white", font='Helvetica 10 bold')
    Label_given_y1.place(x=304, y=44)
    Label_given_y2 = Label(window, text="y2", bg="white", font='Helvetica 10 bold')
    Label_given_y2.place(x=304, y=95)

    # Entry fields and positions
    e1 = Entry(window, width=15, borderwidth=2)
    e1.grid(row=1, column=3, padx=15, pady=15)
    e2 = Entry(window, width=15, borderwidth=2)
    e2.grid(row=2, column=1, padx=15, pady=15)
    e3 = Entry(window, width=15, borderwidth=2)
    e3.grid(row=3, column=1, padx=15, pady=15)
    e4 = Entry(window, width=15, borderwidth=2)
    e4.grid(row=2, column=5, padx=15, pady=15)
    e5 = Entry(window, width=15, borderwidth=2)
    e5.grid(row=3, column=5, padx=15, pady=15)

    display_text = StringVar(window)
    display_text.set("Answer is ")
    myLabel = Label(window, textvariable=display_text, bg="white", font='Helvetica 9 bold')
    myLabel.place(x=136, y=150)

    def Interpolate():
        given_num = float(e1.get())
        right_up = float(e2.get())
        right_down = float(e3.get())
        left_up = float(e4.get())
        left_down = float(e5.get())

        if right_up > right_down:
            right_up, right_down = right_down, right_up

        if left_up > left_down:
            left_up, left_down = left_down, left_up

        interpolated_num = left_up + (given_num - right_up) * ((left_down - left_up) / (right_down - right_up))
        inter_numString = str(interpolated_num)
        display_text.set("Answer is " + "")
        s = display_text.get()
        s += inter_numString
        display_text.set(s)

    # window config
    #window.iconphoto(False, PhotoImage(file='D:\\Python projects\\MISC\\icon.png'))
    window.title("Interpolator")
    window.configure(bg='white')
    window.configure(pady=36)
    window.resizable(False, False)
    get_Interpolation = Button(window, text="Interpolate", command=Interpolate)
    get_Interpolation.place(x=152, y=88)

    # the mainloop function starts the widget/s and executes it until closed
    # anything below it will not be executed until the mainloop is stopped
    window.mainloop()

