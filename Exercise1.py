from tkinter import *
from Interpolator import interwin


def exercise1():
    root = Toplevel()
    #root.iconphoto(False, PhotoImage(file='D:\\Python projects\\MISC\\icon.png'))
    root.configure(bg="white")
    root.geometry("660x410")
    root.resizable(False, False)
    root.title("Exercise 1")



    title = Label(root, text="Exercise 1 - Max cargo at given conditions", font='Helvetica 15 bold', bg="white")
    title.grid(row=0, column=2, padx=100, pady=0)

    # Entries
    constant = Entry(root, width=8, borderwidth=2)
    constant.place(x=35, y=60)
    draft_port = Entry(root, width=8, borderwidth=2)
    draft_port.place(x=145, y=60)
    water_density = Entry(root, width=8, borderwidth=2)
    water_density.place(x=35, y=120)
    provisions = Entry(root, width=8, borderwidth=2)
    provisions.place(x=145, y=120)
    keel_width = Entry(root, width=8, borderwidth=2)
    keel_width.place(x=35, y=180)
    deadweight = Entry(root, width=8, borderwidth=2, bg="white smoke")
    deadweight.place(x=145, y=180)

    # Labels
    ship_constant = Label(root, text="Ship constant", bg="white")
    ship_constant.place(x=25, y=35)
    draft_port_txt = Label(root, text="Max draught at the port", bg="white")
    draft_port_txt.place(x=110, y=35)
    water_density_txt = Label(root, text="Water density t/m3", bg="white")
    water_density_txt.place(x=7, y=95)
    provisions_txt = Label(root, text="Provisions", bg="white")
    provisions_txt.place(x=141, y=95)
    keel_width_txt = Label(root, text="Displacement", bg="white")
    keel_width_txt.place(x=23, y=155)
    deadweight_txt = Label(root, text="Deadweight", bg="white")
    deadweight_txt.place(x=139, y=155)
    answer_pretext = StringVar(root)
    answer_pretext.set("Max cargo that can be loaded:  ")
    answer = Label(root, textvariable=answer_pretext, bg="white")
    answer.place(x=7, y=250)

    explanation = Text(root, height=10, width=50, borderwidth=2)
    explanation.place(x=245,y=40)
    quote = """So the first thing you need to do is to substract your keel width from the given draught,after that open the interpolator (in the upper right corner) and interpolate with your new draught to find the Displacement.
    Input the needed paramaters in the fields,click answer and magic."""
    explanation.insert(END, quote)


    def cargo_sum():
        constant_num = float(constant.get())
        water_density_num = float(water_density.get())
        provisions_num = float(provisions.get())
        displacement_num = float(keel_width.get())
        deadweight_num = float(deadweight.get())

        new_displacement = water_density_num / 1.025 * displacement_num

        max_cargo = new_displacement - (deadweight_num + provisions_num + constant_num)
        max_cargo_txt = str(max_cargo)

        answer_pretext.set("Max cargo that can be loaded:  ")
        cargo1 = answer_pretext.get()
        cargo1 += max_cargo_txt
        answer_pretext.set(cargo1)

    get_cargo = Button(root, text="Answer", bg="white", command=cargo_sum)
    get_cargo.place(x=88, y=220)
    open_interpolator = Button(root,text="Open Interpolator", bg="white", command=interwin)
    open_interpolator.place(x=540, y=5)





    root.mainloop()
