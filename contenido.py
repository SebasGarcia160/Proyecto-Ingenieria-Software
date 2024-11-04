
#!/usr/bin/python
# -*- coding: utf-8 -*-

class Contenido:
    def __init__(self, ID=None, titulos=None, descripcion=None, fecha_creacion=None, autor=None, tipo=None):
        self.ID = ID
        self.titulos = titulos
        self.descripcion = descripcion
        self.fecha_creacion = fecha_creacion
        self.autor = autor
        self.tipo = tipo

    def editar_contenido(self, nuevo_titulo, nueva_descripcion):
        self.titulos = nuevo_titulo
        self.descripcion = nueva_descripcion
        print("Contenido editado.")

    def eliminar_contenido(self):
        # Implementación de eliminación
        print("Contenido eliminado.")
