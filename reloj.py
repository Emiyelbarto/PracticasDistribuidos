from tkinter import *
from tkinter import messagebox
from datetime import datetime
from functools import partial
from edit import *
import threading
import time


class App():
    def checkUpdate(self, id):
        # SI AUN NO ACABA, REPITE EL CICLO HASTA QUE ENCUENTRE QUE YA TERMINO DE REALIZAR LOS CAMBIOS LA VENTANA
        if(not self.ventana_cambios["v%s" % id].consultar()):
            # CUANDO TERMINA DE REALIZAR LOS CAMBIOS, PONE LA BANDERA DE CLOCK ENABLE EN TRUE PARA CONTINUAR CON EL AVANCE DEL RELOJ
            self.clock_enable["clk%s" % id] = True

            # OBTIENE LA NUEVA HORA REGISTRADA EN LA VENTANA DE CAMBIOS
            h, m, s, v = self.ventana_cambios["v%s" % id].get_hora().split(":")

            # ACTUALIZA LA HORA QUE SE TIENE REGISTRADA EN LA LISTA PARA QUE EL HILO TRABAJE CON LA NUEVA HORA
            self.clk_speed = 1/int(v)
            self.horas["reloj%s" % id].set(
                datetime(2021, 1, 1, int(h), int(m), int(s)).strftime("%H:%M:%S"))

    def editar(self, id):
        # AL HACER CLICK SOBRE EL BOTON DE EDITAR SE DETIENE EL RELOJ PONIENDO EN FALSE LA BANDERA REGISTRADA EN LA LISTA DE CLOCK_ENABLE (clk1: false)
        # DE ESTA FORMA LA FUNCION UPDATE NO PODRA ACTUALIZAR EL RELOJ
        self.clock_enable["clk%s" % id] = False
        print("El id %s hizo click" % id)
        print("El reloj tiene velocidad de" % self.clk_speed)
        # EN LA LISTA DE VENTANA CAMBIOS GUARDA LA REFERENCIA AL OBJETO DE LA NUEVA VENTANA CREADA
        # A ESTA VENTANA SE LE ESTA MANDANDO EL ID DEL HILO SOLO PARA MOSTRAR EN EL TITULO "EDITAR EL RELOJ 1"
        # SE LE MANDA LA HORA QUE TIENE REGISTRADA EL RELOJ DEL HILO PARA MOSTRARLA EN LA VENTANA
        # EL ULTIMO ARGUMENTO AHORITA PUSE UN 1, PERO REPRESENTA LA VELOCIDAD CON LA QUE AVANZA EL RELOJ, AQUI DEBERIA IR UNA VARIABLE QUE INDIQUE EL AVANCE DEL RELOJ
        self.ventana_cambios["v%s" % id] = Edit(
            id, self.horas["reloj%s" % id], 1)

    def update(self, id):
        # ESTA LA COPIE TAL CUAL DE LO QUE YA TENIAN HECHO, SOLO AGREGUE EL IF PARA SABER SI EL RELOJ PUEDE AVANZAR O NO
        if self.clock_enable["clk%s" % id]:
            self.d = str(self.horas["reloj%s" % id].get())
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
            # EL VALOR ACTUALIZADO LO GUARDA EN LA LISTA DE LAS HORAS REGISTRADAS PARA CADA HILO (reloj1: '21:30:19')
            self.horas["reloj%s" % id].set(self.d)
        else:
            # CUANDO NO PUEDE AVANZAR, VERIFICA SI LA VENTANA DE CAMBIOS YA TERMINO DE GUARDAR LA NUEVA HORA
            self.checkUpdate(id)

    def new_clock(self, id, vel_clock):
        self.updateWindow = False
        x_label = int()
        y_label = int()

        x_edit = int()
        y_edit = int()

        # DEPENDIENDO DEL IDENTIFICADOR MANDADO COMO ARGUMENTO AL HILO, SABRA EN QUE COORDENADAS PONER EL LABEL PARA MOSTRAR LA HORA Y EL BOTON DE EDITAR
        if id == 0:
            x_label = 160
            y_label = 10
            x_edit = 255
            y_edit = 100
            self.horas["reloj%s" % id] = StringVar()
            # PARA EL RELOJ 0 AJUSTA LA HORA A LA HORA DE LA COMPUTADORA
            self.horas["reloj%s" % id].set(datetime.now().strftime("%H:%M:%S"))

        elif id == 1:
            x_label = 630
            y_label = 10
            x_edit = 725
            y_edit = 100
            self.horas["reloj%s" % id] = StringVar()
            # AJUSTA UNA HORA CUALQUIERA PARA EL RELOJ 1
            self.horas["reloj%s" % id].set(
                datetime(2021, 3, 29, 13, 0, 0).strftime("%H:%M:%S"))

        elif id == 2:
            x_label = 160
            y_label = 210
            x_edit = 255
            y_edit = 300
            self.horas["reloj%s" % id] = StringVar()
            # AJUSTA UNA HORA CUALQUIERA PARA EL RELOJ 2
            self.horas["reloj%s" % id].set(
                datetime(2021, 3, 29, 19, 20, 0).strftime("%H:%M:%S"))

        elif id == 3:
            x_label = 630
            y_label = 210
            x_edit = 725
            y_edit = 300
            self.horas["reloj%s" % id] = StringVar()
            # AJUSTA UNA HORA CUALQUIERA PARA EL RELOJ 3
            self.horas["reloj%s" % id].set(
                datetime(2021, 3, 29, 21, 40, 19).strftime("%H:%M:%S"))

        # CREA LOS ELEMENTOS Y LOS DIBUJA EN LA VENTANA, ESTOS ELEMENTOS YA SON CONTROLADOS COMPLETAMENTE POR EL HILO

        self.elements["lb%s" % id] = Label(
            self.root, textvariable=self.horas["reloj%s" % id], font=("Courier 40 bold"), bg="white")
        self.elements["bt%s" % id] = Button(self.root, text="Editar", command=partial(
            self.editar, id), font=("Arial 12 bold"))
        # EL BOTON DE EDITAR REDIRIGE A LA FUNCION EDITAR Y LE MANDA COMO ARGUMENTO EL ID DEL HILO
        self.elements["lb%s" % id].place(x=x_label, y=y_label)
        self.elements["bt%s" % id].place(x=x_edit, y=y_edit)

        # GUARDA EN LA LISTA DE CLOCK_ENABLE UN VALOR TRUE PARA INDICAR QUE EL RELOJ PUEDE AVANZAR (clk1: true)
        self.clock_enable["clk%s" % id] = True

        # ENTRA AL CICLO INFINITO PARA ACTUALIZAR EL RELOJ CADA SEGUNDO
        while True:
            # Velocidad a la que irá el reloj
            if(vel_clock < 0):
                time.sleep(vel_clock)
                self.update(id)
            else:
                time.sleep(1)
                self.update(id)

    def on_closing(self):
        # MANEJA EL EVENTO DE CERRAR LA VENTANA NADAMAS PARA QUE SE VEA MAS MAMALON
        if messagebox.askokcancel("Salir", "Desea finalizar el programa?"):
            self.root.destroy()

    def __init__(self):
        self.root = Tk()
        self.root.title("Práctica 1")
        self.root.geometry("1000x350")
        self.root.resizable(0, 0)
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)

        # LISTA PARA IDENTIFICAR LOS BOTONES Y LABELS CREADOS POR LOS HILOS
        self.elements = {}
        # LISTA DE HORAS REGISTRADAS PARA CADA HILO
        self.horas = {}
        # Velocidad a la que ira el reloj
        self.clk_speed = 1.0
        # LISTA DE BANDERA PARA CADA HILO QUE INDICA SI SE DETIENE O PUEDE SEGUIR AVANZANDO
        self.clock_enable = {}
        # LISTA PARA GUARDAR LA REFERENCIA DE LA VENTANA CREADA PARA REALIZAR LOS CAMBIOS
        self.ventana_cambios = {}

        self.threads = list()
        for i in range(4):
            self.t = threading.Thread(
                target=self.new_clock, args=(i, self.clk_speed))
            self.threads.append(self.t)
            self.t.setDaemon(True)

            # LANZA EL HILO A LA FUNCION NEW CLOCK, COMO ARGUMENTO LE MANDA EL IDENTIFICADOR DE CADA HILO (0,1,2,3) PARA
            # MANEJAR LAS POSICIONES EN QUE CREA LOS ELEMENTOS DE LA VENTANA Y GUARDAR ELEMENTOS EN LAS LISTAS ANTERIORMENTE DECLARADAS
            self.t.start()

        self.root.mainloop()


a = App()
