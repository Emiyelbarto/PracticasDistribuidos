from tkinter import *
from tkinter import simpledialog
import threading
import sys
import time
import requests


class Reloj():
    h = 0
    m = 0
    s = 0
    run = True
    StringValue = None

    def __init__(self, h, m, s, String=None):
        self.h = h
        self.m = m
        self.s = s
        if(String != None):
            self.StringValue = String

    def check(self):
        if(self.s < 59):
            self.s += 1
        elif(self.s == 59):
            self.s = 0
            if(self.m < 59):
                self.m += 1
            elif(self.m == 59):
                self.m = 0
                self.h += 1

    def increase(self):
        self.check()

    def setTime(self, h, m, s):
        self.h = h
        self.m = m
        self.s = s
        if(self.StringValue != None):
            print(self.getTimeStr())
            self.StringValue.set(self.getTimeStr())
        time.sleep(1)

    def getTimeStr(self):
        horas = str(self.h)
        minu = str(self.m)
        seg = str(self.s)
        if(self.h <= 9):
            horas = "0"+horas
        if(self.m <= 9):
            minu = "0"+minu
        if(self.s <= 9):
            seg = "0"+seg
        return horas + ":" + minu + ":" + seg

    def reset(self):
        self.h = 0
        self.m = 0
        self.s = 0
        if(self.StringValue != None):
            self.StringValue.set("00:00:00")

    def start(self):
        self.run = True
        while self.run:
            self.increase()
            if(self.StringValue != None):
                self.StringValue.set(self.getTimeStr())
            time.sleep(1)

    def stop(self):
        self.run = False


class App():
    textLabel = None
    reloj = None
    hilos = [
        None for i in range(4)
    ]
    url = './índice.png'

    def start(self, no_reloj):
        self.hilos[no_reloj] = threading.Thread(
            target=self.reloj[no_reloj].start,
        )
        self.hilos[no_reloj].start()

    def setTimeEnReloj(self, no_reloj):
        try:
            self.stop(no_reloj)
        except:
            print("No hay hilo asociado en reloj {}".format(no_reloj))

        respuesta = simpledialog.askstring(
            "Input", "Valor del reloj (hh:mm:ss)",
            parent=self.root
        )
        if(respuesta is not None):
            respuesta = respuesta.split(":")
            try:
                h = int(respuesta[0])
                m = int(respuesta[1])
                s = int(respuesta[2])
                self.reloj[no_reloj].setTime(h, m, s)
            except:
                print("Valor incorrecto")
            time.sleep(1)
            self.start(no_reloj)

    def on_closing(self):
        for i in range(len(self.hilos)):
            self.reloj[i].stop()
            #print("Hilo {} cerrado".format(i))
        # self.root.destroy()
        exit()

    def stop(self, no_reloj):
        self.reloj[no_reloj].stop()
        self.hilos[no_reloj].join()

    def __init__(self):
        self.root = Tk()
        self.root.title("Práctica 1")
        self.root.geometry("1000x350")
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.textLabel = [
            StringVar() for i in range(4)
        ]
        for i in range(4):
            self.textLabel[i].set("00:00:00")

        self.reloj = [
            Reloj(0, 0, 0, String=self.textLabel[i]) for i in range(4)
        ]
        modifyIcon = PhotoImage(file=self.url)
        # Resizing image to fit on button
        modifyIcon = modifyIcon.subsample(7, 7)
        # Reloj 1

        self.lb1 = Label(
            self.root, textvariable=self.textLabel[0],
            font=("Courier 40 bold"), bg="white"
        )
        self.bt11 = Button(
            self.root, text="Iniciar",
            command=lambda: self.start(0), font=("Arial 12 bold")
        )
        self.bt21 = Button(
            self.root, text="Detener",
            command=lambda: self.stop(0), font=("Arial 12 bold")
        )
        self.bt31 = Button(
            self.root, text="Reiniciar",
            command=self.reloj[0].reset, font=("Arial 12 bold")
        )

        self.mdbt1 = Button(
            self.root,
            image=modifyIcon,
            height=20,
            width=20,
            command=lambda: self.setTimeEnReloj(0)
        )
        self.lb1.place(x=160, y=10)
        self.bt11.place(x=130, y=100)
        self.bt21.place(x=255, y=100)
        self.bt31.place(x=370, y=100)
        self.mdbt1.place(x=430, y=25)

        # Reloj 2
        self.lb2 = Label(
            self.root, textvariable=self.textLabel[1],
            font=("Courier 40 bold"), bg="white"
        )
        self.bt12 = Button(
            self.root, text="Iniciar",
            command=lambda: self.start(1), font=("Arial 12 bold")
        )
        self.bt22 = Button(
            self.root, text="Detener",
            command=lambda: self.stop(1), font=("Arial 12 bold")
        )
        self.bt32 = Button(
            self.root, text="Reiniciar",
            command=self.reloj[1].reset, font=("Arial 12 bold")
        )
        self.mdbt2 = Button(
            self.root,
            image=modifyIcon,
            height=20,
            width=20,
            command=lambda: self.setTimeEnReloj(1)
        )
        self.lb2.place(x=630, y=10)
        self.bt12.place(x=600, y=100)
        self.bt22.place(x=725, y=100)
        self.bt32.place(x=840, y=100)
        self.mdbt2.place(x=900, y=25)

        # Reloj 3
        self.lb3 = Label(
            self.root, textvariable=self.textLabel[2],
            font=("Courier 40 bold"), bg="white"
        )
        self.bt13 = Button(
            self.root, text="Iniciar",
            command=lambda: self.start(2), font=("Arial 12 bold")
        )
        self.bt23 = Button(
            self.root, text="Detener",
            command=lambda: self.stop(2), font=("Arial 12 bold")
        )
        self.bt33 = Button(
            self.root, text="Reiniciar",
            command=self.reloj[2].reset, font=("Arial 12 bold")
        )
        self.mdbt3 = Button(
            self.root,
            image=modifyIcon,
            height=20,
            width=20,
            command=lambda: self.setTimeEnReloj(2)
        )
        self.lb3.place(x=160, y=210)
        self.bt13.place(x=130, y=300)
        self.bt23.place(x=255, y=300)
        self.bt33.place(x=370, y=300)
        self.mdbt3.place(x=430, y=225)

        # Reloj 4
        self.lb4 = Label(
            self.root, textvariable=self.textLabel[3],
            font=("Courier 40 bold"), bg="white"
        )
        self.bt14 = Button(
            self.root, text="Iniciar",
            command=lambda: self.start(3), font=("Arial 12 bold")
        )
        self.bt24 = Button(
            self.root, text="Detener",
            command=lambda: self.stop(4), font=("Arial 12 bold")
        )
        self.bt34 = Button(
            self.root, text="Reiniciar",
            command=self.reloj[3].reset, font=("Arial 12 bold")
        )
        self.mdbt4 = Button(
            self.root,
            image=modifyIcon,
            height=20,
            width=20,
            command=lambda: self.setTimeEnReloj(3)
        )
        self.lb4.place(x=630, y=210)
        self.bt14.place(x=600, y=300)
        self.bt24.place(x=725, y=300)
        self.bt34.place(x=840, y=300)
        self.mdbt4.place(x=900, y=225)

        self.root.mainloop()


a = App()
