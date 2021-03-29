from tkinter import *

class Edit():
    def consultar(self):
        return self.isOpen

    def get_hora(self):
        return self.hora_guardada

    def guardar_cambios(self):
        self.hora_guardada = self.hora_a.get() + ":" + self.minu_a.get() + ":" + self.segu_a.get() + ":" + self.vel_r.get()
        #                       HORA                    MINUTO                  SEGUNDO                     NUEVA_VELOCIDAD
        #AL PONER LA BANDERA ISOPEN EN FALSE, EL PROGRAMA PRINCIPAL PODRA LEER LA NUEVA HORA REGISTRADA POR LA VENTANA DE CAMBIOS
        self.isOpen = False
        self.root.destroy()


    def __init__(self, id, hora, velocidad):
        self.isOpen = True
        self.hora_guardada = ""

        self.root = Tk()
        self.root.title("Editar reloj %s" %(id + 1))
        self.root.geometry("300x350")
        self.hora_str = str(hora.get())

        self.h, self.m, self.s = self.hora_str.split(":")

        self.hora_a = StringVar(self.root)
        self.hora_a.set(self.h)

        self.minu_a = StringVar(self.root)
        self.minu_a.set(self.m)

        self.segu_a = StringVar(self.root)
        self.segu_a.set(self.s)

        self.vel_r = StringVar(self.root)
        self.vel_r.set(velocidad)

        Label(self.root,text="").pack()
        Label(self.root,text="Hora: ").pack()
        self.hora = Spinbox(self.root, from_=0, to=23, textvariable=self.hora_a, wrap=True, width=10)
        self.hora.pack()

        Label(self.root,text="").pack()
        Label(self.root,text="Minuto: ").pack()
        self.minuto = Spinbox(self.root, from_=0, to=59, textvariable=self.minu_a, wrap=True, width=10)
        self.minuto.pack()

        Label(self.root,text="").pack()
        Label(self.root,text="Segundo: ").pack()
        self.segundo = Spinbox(self.root, from_=0, to=59, textvariable=self.segu_a, wrap=True, width=10)
        self.segundo.pack()

        Label(self.root,text="").pack()
        Label(self.root, text="Velocidad en segundos: ").pack()
        self.velocidad_rel = Spinbox(self.root, from_=1, to=10, textvariable=self.vel_r, wrap=True, width=10)
        self.velocidad_rel.pack()

        Label(self.root,text="").pack()
        self.guardar = Button(self.root, text="Guardar cambios", command=self.guardar_cambios)
        self.guardar.pack()

        #self.root.mainloop()