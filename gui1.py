from tkinter import Entry, Tk, Label, Button, ttk
import os
import webbrowser
class VentanaEjemplo:
    def __init__(self, master):
        self.master = master
        master.title("Una simple interfaz grafica || webos xd ")

        self.etiqueta = Label(master, text="ESTA ES LA PRIMER VENTANA!")
        self.etiqueta.pack()

        self.botonSaludo = Button(master, text="Saludar", command = self.saludar)
        self.botonSaludo.pack() 

        self.botonApagar = Button(master, text="Shutdown", command = self.shutdown)
        self.botonApagar.pack()

        self.botonReiniciar = Button(master, text="Restart", command = self.restart)
        self.botonReiniciar.pack()

        self.botonSalir = Button(master, text="Salir", command = self.salir)
        self.botonSalir.pack()

        self.botonOpera = Button(master, text="Abrir Opera", command= self.Opera)
        self.botonOpera.pack()

    def saludar(self):
        root2 = Tk()
        miVentanta2 = ventana2(root2)
        root2.mainloop()

    def shutdown(self):
        root3 = Tk()
        miVentana3 = apagar(root3)
        root3.mainloop()

    def restart(self):
        root4 = Tk()
        miVentana3 = apagar(root4)
        root4.mainloop()

    def salir(self):
        exit()

    def Opera(self):
        root5 = Tk()
        miVentana4 = video(root5)
        root5.mainloop()

class ventana2:
    def __init__(self2, master2):
        self2.master2 = master2
        master2.title("Un simple saludador")

        self2.etiqueta2 = Label(master2, text="Helllo xd")
        self2.etiqueta2.pack()

class apagar:
    def __init__(self3, master3):
        self3.master3 = master3
        master3.title("Ventana de apagar")

        self3.etiqueta3 = Label(master3, text="Esta seguro?")
        self3.etiqueta3.pack()

        self3.botonSi = Button(master3, text="Yes", command= self3.apagar)
        self3.botonSi.pack()

        self3.botonNo = Button(master3, text="No", command= self3.regresar)
        self3.botonNo.pack()

    def apagar(self3):
        os.system("shutdown /s /t 1")
    
    def regresar(self3):
        exit()

class reiniciar:
    def __init__(self4, master4):
        self4.master4 = master4
        master4.title("Ventana de reiniciar")

        self4.etiqueta = Label(master4, text="Esta seguro?")
        self4.etiqueta.pack()

        self4.botonSi = Button(master4, text="Yes", command= self4.reiniciar)
        self4.botonSi.pack()

        self4.botonNo = Button(master4, text="No", command= self4.regresar)
        self4.botonNo.pack()

    def reiniciar(self4):
        os.system("shutdown /r /t 1")

    def regresar(self):
        exit()

class video:
    
    def __init__(self, master):
        self.master = master
        master.title("Ventana para videos")

        self.etiqueta = Label(master, text="Ingresa el link para abrir")
        self.etiqueta.pack()

        self.insertar = Entry(master)
        self.insertar.pack()
    
        self.botonIngresar = Button(master, text="Abrir link", command= self.ingresar)
        self.botonIngresar.pack()

    def ingresar(self):
        webbrowser.open(self.insertar.get(), new= 1, autoraise= True)

    def regresar(self):
        os.link

class YTDownloader:
    def __init__(self, master):
        self.master = master
        master.title("Ventana para descargar videos")

        self.etiqueta = Label(master, text="Ingresa el link del video que quieres descargar")
        self.etiqueta.pack()

        self.link = Entry(master)
        self.link.pack()

        self.botonDownload = Button(master, text="Descargar", command= self.Download)
        self.botonDownload.pack()

    def ingresarWebDownload(self):
        webbrowser.open("www.y2mate.com", new= 1, autoraise= True)
        
root = Tk()
miVentana = VentanaEjemplo(root)
root.mainloop()