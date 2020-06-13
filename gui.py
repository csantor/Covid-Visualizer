from tkinter import *
import visualize_corona


def button_pressed():
    population = int(en_pop.get())
    days = int(en_days.get())
    contact_rate = int(en_cont_rate.get())
    infected = int(en_inf.get())
    removed = int(en_rem.get())
    visualize_corona.SimVirus(days=days, population=population, inf=infected,
                                contact_rate=contact_rate, rem=removed)


window = Tk()

window.title('Covid-19 Visualizer')
window.geometry('370x200')

Label(window, text="Population").place(x=0)
Label(window, text="Days").place(x=70)
Label(window, text="Contact Rate").place(x=140)
Label(window, text="Infected").place(x=220)
Label(window, text="Removed").place(x=290)

en_pop = Entry(window, width=10)
en_days = Entry(window, width=10)
en_cont_rate = Entry(window, width=10)
en_inf = Entry(window, width=10)
en_rem = Entry(window, width=10)

en_pop.place(x=0, y=20)
en_days.place(x=70, y=20)
en_cont_rate.place(x=140, y=20)
en_inf.place(x=220, y=20)
en_rem.place(x=290, y=20)

en_pop.insert(END, 1000)
en_days.insert(END, 160)
en_cont_rate.insert(END, 5)
en_inf.insert(END, 1)
en_rem.insert(END, 0)

sim_button = Button(window, text='Run sim', command=button_pressed)
sim_button.place(x=140, y=40)

instructions = 'This is a naive model on Covid-19 spreading based on the SIR model.\n ' \
               'To see the graph choose values for the:\n' \
               '1)Population, \n' \
               '2)Days you want the model to run,\n' \
               '3)Contact rate (how many people someone meets in a day, \n' \
               'for example if quarantined you can set it to 0' \
               'or 1), \n' \
               '4)Infected(initialize infected people at the start of the spread\n'\
               '5)Removed(how many were already recovered or dead)'

Label(window, text=instructions).place(x=0, y=70)
window.mainloop()
