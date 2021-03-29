from tkinter import *
import sys
import time

global count
count = 0


class App():

    def reset(self):
        global count
        count = 1
        self.t.set('00:00:00')

    def start(self):
        global count
        count = 0
        self.timer()

    def stop(self):
        global count
        count = 1

    def timer(self):
        global count
        if(count == 0):
            self.d = str(self.t.get())
            h, m, s = map(int, self.d.split(":"))

            h = int(h)
            m = int(m)
            s = int(s)
            if(s < 59):
                s += 1
            elif(s == 59):
                s = 0
                if(m < 59):
                    m += 1
                elif(m == 59):
                    m = 0
                    h += 1

            if(h < 10):
                h = str(0)+str(h)
            else:
                h = str(h)

            if(m < 10):
                m = str(0)+str(m)
            else:
                m = str(m)
            if(s < 10):
                s = str(0)+str(s)
            else:
                s = str(s)
            self.d = h+":"+m+":"+s

            self.t.set(self.d)

            if(self.d == "24:00:00"):
                self.reset()
                count = 0
            if(count == 0):
                self.root.after(1000, self.timer)

    def update_clock(self):
        #now = time.strftime("%H:%M:%S")
        # self.label.configure(text=now)
        #self.label.place(x=160, y=200)
        self.root.after(1000, self.update_clock)

    def __init__(self):
        self.root = Tk()
        self.root.title("Práctica 1")
        self.root.geometry("1000x350")
        self.t = StringVar()
        self.t.set("14:40:57")

        # Reloj 1
        self.lb1 = Label(self.root, textvariable=self.t,
                         font=("Courier 40 bold"), bg="white")
        self.bt11 = Button(self.root, text="Iniciar",
                           command=self.start, font=("Arial 12 bold"))
        self.bt21 = Button(self.root, text="Detener",
                           command=self.stop, font=("Arial 12 bold"))
        self.bt31 = Button(self.root, text="Reiniciar",
                           command=self.reset, font=("Arial 12 bold"))
        self.lb1.place(x=160, y=10)
        self.bt11.place(x=130, y=100)
        self.bt21.place(x=255, y=100)
        self.bt31.place(x=370, y=100)

        # Reloj 2
        self.lb2 = Label(self.root, textvariable=self.t,
                         font=("Courier 40 bold"), bg="white")
        self.bt12 = Button(self.root, text="Iniciar",
                           command=self.start, font=("Arial 12 bold"))
        self.bt22 = Button(self.root, text="Detener",
                           command=self.stop, font=("Arial 12 bold"))
        self.bt32 = Button(self.root, text="Reiniciar",
                           command=self.reset, font=("Arial 12 bold"))
        self.lb2.place(x=630, y=10)
        self.bt12.place(x=600, y=100)
        self.bt22.place(x=725, y=100)
        self.bt32.place(x=840, y=100)

        # Reloj 3
        self.lb3 = Label(self.root, textvariable=self.t,
                         font=("Courier 40 bold"), bg="white")
        self.bt13 = Button(self.root, text="Iniciar",
                           command=self.start, font=("Arial 12 bold"))
        self.bt23 = Button(self.root, text="Detener",
                           command=self.stop, font=("Arial 12 bold"))
        self.bt33 = Button(self.root, text="Reiniciar",
                           command=self.reset, font=("Arial 12 bold"))
        self.lb3.place(x=160, y=210)
        self.bt13.place(x=130, y=300)
        self.bt23.place(x=255, y=300)
        self.bt33.place(x=370, y=300)

        # Reloj 4
        self.lb4 = Label(self.root, textvariable=self.t,
                         font=("Courier 40 bold"), bg="white")
        self.bt14 = Button(self.root, text="Iniciar",
                           command=self.start, font=("Arial 12 bold"))
        self.bt24 = Button(self.root, text="Detener",
                           command=self.stop, font=("Arial 12 bold"))
        self.bt34 = Button(self.root, text="Reiniciar",
                           command=self.reset, font=("Arial 12 bold"))
        self.lb4.place(x=630, y=210)
        self.bt14.place(x=600, y=300)
        self.bt24.place(x=725, y=300)
        self.bt34.place(x=840, y=300)

        #self.label = Label(self.root, text="", font=("Courier 40 bold"))
        self.update_clock()
        self.root.mainloop()


a = App()
