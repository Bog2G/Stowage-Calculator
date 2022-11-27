from tkinter import *
from Interpolator import interwin


def exer2():
    root3 = Toplevel()
   # root3.iconphoto(False, PhotoImage(file='D:\\Python projects\\MISC\\icon.png'))
    root3.configure(bg="white")
    root3.resizable(False, False)
    root3.title("Exercise 2")
    root3.geometry("660x410")

    # Title Label
    title = Label(root3, text="Exercise 2 - Expected and middle draught", font='Helvetica 15 bold', bg="white")
    title.grid(row=0, column=2, padx=130, pady=0)

    #Vars
    var1 = DoubleVar(root3)
    var1.set(0)
    var2 = DoubleVar(root3)
    var2.set(0)
    var3 = DoubleVar(root3)
    var3.set(0)
    var4 = DoubleVar(root3)
    var4.set(0)
    # Entries
    cargo = Entry(root3, width=8, borderwidth=2, textvariable=var1)
    cargo.place(x=145, y=240)
    constant = Entry(root3, width=8, borderwidth=2, textvariable=var2)
    constant.place(x=35, y=60)
    draft_port = Entry(root3, width=8, borderwidth=2)
    draft_port.place(x=145, y=60)
    water_density = Entry(root3, width=8, borderwidth=2)
    water_density.place(x=35, y=120)
    provisions = Entry(root3, width=8, borderwidth=2, textvariable=var3)
    provisions.place(x=145, y=120)
    keel_width = Entry(root3, width=8, borderwidth=2)
    keel_width.place(x=35, y=180)
    deadweight = Entry(root3, width=8, borderwidth=2, textvariable=var4 )
    deadweight.place(x=145, y=180)

    displacement_sum = DoubleVar(root3)


    def sum_displace(*args):
         try:
            displacement_sum.set(var1.get() + var2.get() + var3.get() + var4.get())
         except:
             pass


    var1.trace('w', sum_displace)
    var2.trace('w', sum_displace)
    var3.trace('w', sum_displace)
    var4.trace('w', sum_displace)



    displacement = Entry(root3, width=8, borderwidth=2, textvariable=displacement_sum)
    displacement.place(x=35, y=240)

    # Labels
    ship_constant = Label(root3, text="Ship constant", bg="white")
    ship_constant.place(x=25, y=35)
    draft_port_txt = Label(root3, text="Interpolated Draught", bg="white")
    draft_port_txt.place(x=121, y=35)
    water_density_txt = Label(root3, text="Water density t/m3", bg="white")
    water_density_txt.place(x=7, y=95)
    provisions_txt = Label(root3, text="Provisions", bg="white")
    provisions_txt.place(x=141, y=95)
    keel_width_txt = Label(root3, text="TPCI", bg="white")
    keel_width_txt.place(x=49, y=155)
    deadweight_txt = Label(root3, text="Deadweight", bg="white")
    deadweight_txt.place(x=139, y=155)
    displacement_txt = Label(root3, text="Displacement", bg="white")
    displacement_txt.place(x=25, y=215)
    cargo_txt = Label(root3, text="Given Cargo", bg="white")
    cargo_txt.place(x=137, y=215)
    answer_pretext = StringVar(root3)
    answer_pretext.set("Theoritical Draught: " + "\n" + "Draught in the middle: ")
    answer = Label(root3, textvariable=answer_pretext, bg="white")
    answer.place(x=7, y=315)


    def getSums():
        water_density_num = float(water_density.get())
        tpci_num = float(keel_width.get())
        inter_draft_num = float(draft_port.get())
        displacement_num = float(displacement.get())

        answer_pretext.set("Theoretical Draught: " + "\n" + "Draught in the middle: ")
        sum = displacement_num * (1.025 - water_density_num) / ((water_density_num * tpci_num) * 100)
        theory_draught = inter_draft_num + sum
        middle_draught = theory_draught + 0.026

        s1 = str(theory_draught)
        s2 = str(middle_draught)

        answer_pretext.set("Theoretical Draught: " + s1 + "\n" + "Draught in the middle: " + s2)


    # Buttons
    get_cargo = Button(root3, text="Answer", bg="white", command=getSums)
    get_cargo.place(x=88, y=285)
    open_interpolator = Button(root3, text="Open Interpolator", bg="white", command=interwin)
    open_interpolator.place(x=540, y=5)


    # explain
    explanation = Text(root3, height=10, width=49, borderwidth=2)
    explanation.place(x=241, y=40)
    quote = """So first off fill your ship given information so you can get your displacement and after that open the interpolator(right up corner) and find with the displacement your Draught and TPCI.
     After that fill them in and click the answer button and let the program do it's magic. 
     IMPORTANT!!  
     ( For the purpose of this exercise the keel width is always 0.026)"""
    explanation.insert(END, quote)


    root3.mainloop()
