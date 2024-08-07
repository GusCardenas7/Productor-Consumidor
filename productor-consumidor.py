""" 
Alumno:
Cardenas Reyes Gustavo Angel 217575511
"""

"""  
Significado de cada color:
Blanco = Titulos Y avisos importantes
Verde = Productor
Rojo = Consumidor
Amarillo = Posicion tanto del productor y consumidor
Cyan = Productos a colocar y consumir
Azul = Cuando el productor y consumidor se encuentra durmiendo
"""

# Librerias necesarias para la ejecucion
import random
from time import sleep
import sys
from colorama import init, Fore
import keyboard as kb

init()

print(Fore.WHITE+f"-------PRODUCTOR-CONSUMIDOR-------")

# Clase Productor 
class Productor:
    def __init__(self):
        self.estado = False
        self.producto = " P "

    def GetEstadoPro(self):
        return self.estado

    def OcuparPro(self):
        self.estado = True
    
    def DesocuparPro(self):
        self.estado = False
    
    def SetTiempoPro(self, tiempoPro):
         self.tiempo = tiempoPro

    def GetTiempoPro(self):
         return self.tiempo
    
    def ColocarProducto(self):
         return self.producto

# Clase Comsumidor 
class Consumidor:
    def __init__(self):
        self.estado = False
        self.consumir = " _ "

    def GetEstadoCon(self):
        return self.estado

    def OcuparCon(self):
        self.estado = True
    
    def DesocuparCon(self):
        self.estado = False
    
    def SetTiempoCon(self, tiempoCon):
         self.tiempo = tiempoCon

    def GetTiempoCon(self):
         return self.tiempo
    
    def Consumir(self):
         return self.consumir
    
# Funcion de impresion del contendor
def imprimirContenedor(contador, listaContenedor):
    for i in listaContenedor:
        if(contador % 5 == 0):
            print(i)
            sys.stdout.flush()
            sleep(0.5)
        else:
            print(i, end="")
            sys.stdout.flush()
            sleep(0.5)
        contador+=1

# Clase Tiempo
class Tiempo:
    def __init__(self):
        self.bandera = False
    def countdown(self, num_of_secs):
        while num_of_secs:
            m, s = divmod(num_of_secs, 60)
            min_sec_format = '{:02d}:{:02d}'.format(m, s)
            print(min_sec_format)
            sleep(1)
            num_of_secs -= 1
            if(num_of_secs==0):
                print(Fore.WHITE+f"Terminó")
                self.bandera = True
    def BanderaTermino(self):
        return self.bandera
    def SetBandera(self):
        self.bandera = False
        
# Funcion para buscar espacios
def buscarEspacios(contador, listaContenedor):
    for i in listaContenedor:
        if(i == " _ "):
            contador+=1

    return contador-1

#  Funcion para buscar productos
def buscarProductos(contador, listaContenedor):
    for i in listaContenedor:
        if(i == " P "):
            contador+=1

    return contador-1

# Funcion contenedor
def Contenedor():
    capacidad = 25
    espacios = " _ "
    hayEspacio = True
    hayProductos = False
    contador = 1
    listaContenedor = []
    pro = Productor()
    con = Consumidor()
    contadorPro = 0
    contadorCon = 0

    # Creando del contenedor
    while contador <= capacidad:
        listaContenedor.append(espacios)
        contador+=1

    while not kb.is_pressed('q'):
        contador2 = 1
        compEspacio = buscarEspacios(contador2,listaContenedor)
        if(compEspacio == 0):
            hayEspacio = False
        else:
            hayEspacio = True

        contador3 = 1
        compProductos = buscarProductos(contador3,listaContenedor)
        if(compProductos == 0):
            hayProductos = False
        else:
            hayProductos = True
        volado = random.randint(1,10)
        if(volado % 2 == 0):
            
            print(Fore.GREEN+f"El productor está intentando entrar al contenedor...")
            sleep(0.5)
            if(hayEspacio == True and con.GetEstadoCon() == False):
                print("------------------------------------------------------------------------------------------------------")
                print(Fore.WHITE+f"Si hay espacio y el consumidor no está dentro, por lo que el productor empezará a trabajar")
                print(Fore.GREEN+f"El productor está trabajando...")
                print("------------------------------------------------------------------------------------------------------")
                pro.OcuparPro()
                pro.SetTiempoPro(random.randint(1,10))
                cantidadProductosAColocar = random.randint(1,5)
                print("------------------------------------------------------------------------------------------------------")
                print(Fore.CYAN+f"\nProductos a colocar: {cantidadProductosAColocar}")

                num_of_secs = pro.GetTiempoPro()
                while num_of_secs:
                    # El consumidor puede entrar mientras trabaja el productor
                    contador3 = 1
                    compProductos = buscarProductos(contador3,listaContenedor)
                    if(compProductos == 0):
                        hayProductos = False
                    else:
                        hayProductos = True
                    volado = random.randint(1,10)
                    if(volado % 2 == 0):
                        print("------------------------------------------------------------------------------------------------------")
                        print(Fore.RED+f"El consumidor está intentando entrar al contenedor...")
                        print("------------------------------------------------------------------------------------------------------")
                        sleep(0.5)
                        if(hayProductos == True and pro.GetEstadoPro() == True):
                            print("------------------------------------------------------------------------------------------------------")
                            print(Fore.WHITE+f"Si hay productos, pero el productor está dentro, por lo que el consumidor irá a dormir")
                            print(Fore.BLUE+f"El consumidor está durmiendo...")
                            print("------------------------------------------------------------------------------------------------------")
                        else:
                            print("------------------------------------------------------------------------------------------------------")
                            print(Fore.WHITE+f"No hay productos y el productor está dentro, por lo que el consumidor irá a dormir")
                            print(Fore.BLUE+f"El consumidor está durmiendo...")
                            print("------------------------------------------------------------------------------------------------------")

                    contador2 = 1
                    compEspacio = buscarEspacios(contador2,listaContenedor)
                    if(compEspacio == 0):
                        hayEspacio = False
                    else:
                        hayEspacio = True
                    # El productor empieza a trabajar
                    if(cantidadProductosAColocar != 0 and hayEspacio == True):
                        listaContenedor[contadorPro]=pro.ColocarProducto()
                        cantidadProductosAColocar-=1
                        if(contadorPro==24):
                            contadorPro=0
                        else:
                            contadorPro+=1
                    else:
                        cantidadProductosAColocar = random.randint(1,5)
                        print("------------------------------------------------------------------------------------------------------")
                        print(Fore.CYAN+f"\nProductos a colocar: {cantidadProductosAColocar}")
                    m, s = divmod(num_of_secs, 60)
                    min_sec_format = '{:02d}:{:02d}'.format(m, s)
                    print(min_sec_format)
                    sleep(1)
                    num_of_secs -= 1
                
                    # Si se termina el tiempo del productor, entonces el productor se pone a dormir
                    if(num_of_secs==0):
                        print("------------------------------------------------------------------------------------------------------")
                        print(Fore.WHITE+f"Terminó el tiempo del productor")
                        print(Fore.BLUE+f"El productor está durmiendo...")
                        print("------------------------------------------------------------------------------------------------------")
                print(Fore.YELLOW+f"\nPosición actual del productor: {contadorPro}")
                contador4 = 1
                imprimirContenedor(contador4, listaContenedor)
                pro.DesocuparPro()
            elif(hayEspacio == False and con.GetEstadoCon() == False):
                print("------------------------------------------------------------------------------------------------------")
                print(Fore.WHITE+f"El consumidor no está dentro, pero no hay espacio en el contenedor, por lo que el productor irá a dormir")
                print(Fore.BLUE+f"El productor está durmiendo...")
                print("------------------------------------------------------------------------------------------------------")
            elif(hayEspacio == True and con.GetEstadoCon() == True):
                print("------------------------------------------------------------------------------------------------------")
                print(Fore.WHITE+f"Si hay espacio, pero el consumidor está dentro, por lo que el productor irá a dormir")
                print("El productor está durmiendo...")
                print("------------------------------------------------------------------------------------------------------")
            else:
                print("------------------------------------------------------------------------------------------------------")
                print(Fore.WHITE+f"No hay espacio y el consumidor está dentro, por lo que el productor irá a dormir")
                print(Fore.BLUE+f"El productor está durmiendo...")
                print("------------------------------------------------------------------------------------------------------")
        else:
            print("------------------------------------------------------------------------------------------------------")
            print(Fore.RED+f"El consumidor está intentando entrar al contenedor...")
            sleep(0.5)
            if(hayProductos == True and pro.GetEstadoPro() == False):
                print("------------------------------------------------------------------------------------------------------")
                print(Fore.WHITE+f"Si hay productos y el productor no está dentro, por lo que el consumidor empezará a trabajar")
                print(Fore.RED+f"El consumidor está trabajando...")
                print("------------------------------------------------------------------------------------------------------")
                con.OcuparCon()
                con.SetTiempoCon(random.randint(1,10))
                cantidadProductosAConsumir = random.randint(1,5)
                print(Fore.CYAN+f"\nProductos a consumir: {cantidadProductosAConsumir}")
                num_of_secs = con.GetTiempoCon()
                while num_of_secs:
                    # El productor puede entrar mientras trabaja el consumidor
                    contador2 = 1
                    compEspacio = buscarEspacios(contador2,listaContenedor)
                    if(compEspacio == 0):
                        hayEspacio = False
                    else:
                        hayEspacio = True
                    volado = random.randint(1,10)
                    if(volado % 2 == 0):
                        print("------------------------------------------------------------------------------------------------------")
                        print(Fore.GREEN+f"El productor está intentando entrar al contenedor...")
                        sleep(0.5)
                        if(hayEspacio == True and con.GetEstadoCon() == True):
                            print("------------------------------------------------------------------------------------------------------")
                            print(Fore.WHITE+f"Si hay espacio, pero el consumidor está dentro, por lo que el productor irá a dormir")                           
                            print(Fore.BLUE+f"El productor está durmiendo...")
                            print("------------------------------------------------------------------------------------------------------")
                        else:
                            print("------------------------------------------------------------------------------------------------------")
                            print(Fore.WHITE+f"No hay espacio y el consumidor está dentro, por lo que el productor irá a dormir")                           
                            print(Fore.BLUE+f"El productor está durmiendo...")
                            print("------------------------------------------------------------------------------------------------------")
                    
                    contador3 = 1
                    compProductos = buscarProductos(contador3,listaContenedor)
                    if(compProductos == 0):
                        hayProductos = False
                    else:
                        hayProductos = True
                    # El consumidor empieza a trabajar
                    if(cantidadProductosAConsumir != 0 and hayProductos == True):
                        listaContenedor[contadorCon]=con.Consumir()
                        cantidadProductosAConsumir-=1
                        if(contadorCon==24):
                            contadorCon=0
                        else:
                            contadorCon+=1
                    else:
                        cantidadProductosAConsumir = random.randint(1,5)
                        print("------------------------------------------------------------------------------------------------------")
                        print(Fore.CYAN+f"\nProductos a consumir: {cantidadProductosAConsumir}")
                    m, s = divmod(num_of_secs, 60)
                    min_sec_format = '{:02d}:{:02d}'.format(m, s)
                    print(min_sec_format)
                    sleep(1)
                    num_of_secs -= 1
                    
                    # Si se termina el tiempo del consumidor, entonces el consumidor se pone a dormir
                    if(num_of_secs==0):
                        print("------------------------------------------------------------------------------------------------------")
                        print(Fore.WHITE+f"Terminó el tiempo del consumidor")
                        print(Fore.BLUE+f"El consumidor está durmiendo...")
                        print("------------------------------------------------------------------------------------------------------")
                print(Fore.YELLOW+f"\nPosición actual del consumidor: {contadorCon}")
                contador5 = 1
                imprimirContenedor(contador5, listaContenedor)
                con.DesocuparCon()
            elif(hayProductos == False and pro.GetEstadoPro() == False):
                print("------------------------------------------------------------------------------------------------------")
                print(Fore.WHITE+f"El productor no está dentro, pero no hay productos en el contenedor, por lo que el consumidor irá a dormir")
                print(Fore.BLUE+f"El consumidor está durmiendo...")
                print("------------------------------------------------------------------------------------------------------")
            elif(hayProductos == True and pro.GetEstadoPro() == True):
                print("------------------------------------------------------------------------------------------------------")
                print(Fore.WHITE+f"Si hay productos, pero el productor está dentro, por lo que el consumidor irá a dormir")
                print(Fore.BLUE+f"El consumidor está durmiendo...")
                print("------------------------------------------------------------------------------------------------------")
            else:
                print("------------------------------------------------------------------------------------------------------")
                print(Fore.WHITE+f"No hay productos y el productor está dentro, por lo que el consumidor irá a dormir")
                print(Fore.BLUE+f"El consumidor está durmiendo...")
                print("------------------------------------------------------------------------------------------------------")

# Ejecucion del programa
if __name__ == '__main__':
    Contenedor()