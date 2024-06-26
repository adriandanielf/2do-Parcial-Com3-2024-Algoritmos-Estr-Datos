#ejercicio1

from datetime import date, timedelta

class Fecha:
    def __init__(self, dia=None, mes=None, año=None):
        if dia is None or mes is None or año is None:
            hoy = date.today()
            self.dia = hoy.day
            self.mes = hoy.month
            self.año = hoy.year
        else:
            self.dia = dia
            self.mes = mes
            self.año = año

    def __str__(self):
        return f"{self.dia:02d}/{self.mes:02d}/{self.año}"

    def __add__(self, days):
        fecha_actual = date(self.año, self.mes, self.dia)
        nueva_fecha = fecha_actual + timedelta(days=days)
        return Fecha(nueva_fecha.day, nueva_fecha.month, nueva_fecha.year)

    def __eq__(self, otra):
        return self.dia == otra.dia and self.mes == otra.mes and self.año == otra.año

    def calcular_dif_fecha(self, otra):
        fecha1 = date(self.año, self.mes, self.dia)
        fecha2 = date(otra.año, otra.mes, otra.dia)
        return abs((fecha2 - fecha1).days)



#ejercicio2


from datetime import date

class Alumno(dict):
    def __init__(self, nombre, dni, fecha_ingreso, carrera):
        super().__init__()
        self["Nombre"] = nombre
        self["DNI"] = dni
        self["FechaIngreso"] = fecha_ingreso
        self["Carrera"] = carrera

    def __str__(self):
        return (f"Nombre: {self['Nombre']}, DNI: {self['DNI']}, Fecha de Ingreso: {self['FechaIngreso']}, "
                f"Carrera: {self['Carrera']}")

    def __eq__(self, otro):
        return (self["Nombre"] == otro["Nombre"] and self["DNI"] == otro["DNI"] and 
                self["FechaIngreso"] == otro["FechaIngreso"] and self["Carrera"] == otro["Carrera"])

    def cambiar_datos(self, **kwargs):
        for key, value in kwargs.items():
            if key in self:
                self[key] = value
    def antiguedad(self):
        hoy = Fecha()
        return hoy.calcular_dif_fecha(self["FechaIngreso"])

#ejercicio3

import random
from datetime import date

class Nodo:
    def __init__(self, dato=None):
        self.dato = dato
        self.siguiente = None
        self.anterior = None

class ListaDoblementeEnlazada:
    def __init__(self):
        self.primero = None
        self.ultimo = None

    def insertar_al_final(self, dato):
        nuevo_nodo = Nodo(dato)
        if self.ultimo is None:
            self.primero = self.ultimo = nuevo_nodo
        else:
            self.ultimo.siguiente = nuevo_nodo
            nuevo_nodo.anterior = self.ultimo
            self.ultimo = nuevo_nodo

    def __iter__(self):
        return ListaDoblementeEnlazadaIterador(self.primero)

    def lista_ejemplo(self):
        nombres = ["Fernando", "Dario", "Miguel", "Elena"]
        carreras = ["Matematica", "Programacion", "Abogacia", "Ingles"]
        lista = ListaDoblementeEnlazada()
        for _ in range(10):
            nombre = random.choice(nombres)
            dni = random.randint(10000000, 40000000)
            fecha_ingreso = Fecha(random.randint(1, 28), random.randint(1, 12), random.randint(2015, 2023))
            carrera = random.choice(carreras)
            alumno = Alumno(nombre, dni, fecha_ingreso, carrera)
            lista.insertar_al_final(alumno)
        return lista

class ListaDoblementeEnlazadaIterador:
    def __init__(self, inicio):
        self.actual = inicio

    def __iter__(self):
        return self

    def __next__(self):
        if self.actual is None:
            raise StopIteration
        else:
            dato = self.actual.dato
            self.actual = self.actual.siguiente
            return dato


#ejercicio4

class ListaDoblementeEnlazada:
    

    def ordenar_por_fecha_ingreso(self):
        if self.primero is None:
            return

        cambiado = True
        while cambiado:
            cambiado = False
            nodo_actual = self.primero

            while nodo_actual.siguiente is not None:
                if nodo_actual.dato["FechaIngreso"] > nodo_actual.siguiente.dato["FechaIngreso"]:
                    nodo_actual.dato, nodo_actual.siguiente.dato = nodo_actual.siguiente.dato, nodo_actual.dato
                    cambiado = True
                nodo_actual = nodo_actual.siguiente



#ejercicio5

import os
import pickle

def crear_directorio_y_guardar_lista(directorio, archivo, lista):
    try:
        os.makedirs(directorio, exist_ok=True)
        ruta_archivo = os.path.join(directorio, archivo)
        with open(ruta_archivo, 'wb') as f:
            pickle.dump(lista, f)
    except Exception as e:
        print(f"Error al crear directorio o guardar archivo: {e}")

def mover_directorio(origen, destino):
    try:
        os.rename(origen, destino)
    except Exception as e:
        print(f"Error al mover el directorio: {e}")

def borrar_directorio_y_archivo(directorio):
    try:
        for archivo in os.listdir(directorio):
            ruta_archivo = os.path.join(directorio, archivo)
            os.remove(ruta_archivo)
        os.rmdir(directorio)
    except Exception as e:
        print(f"Error al borrar archivo o directorio: {e}")

crear_directorio_y_guardar_lista('directorio_original', 'lista_alumnos.pkl', lista)

mover_directorio('nuevo_directorio')

borrar_directorio_y_archivo('nuevo_directorio')
