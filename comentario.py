#!/usr/bin/python
# -*- coding: utf-8 -*-

class Comentario:
    def __init__(self, ID=None, contenido=None, fecha_creacion=None, autor=None):
        self.ID = ID
        self.contenido = contenido
        self.fecha_creacion = fecha_creacion
        self.autor = autor

    def editar_comentario(self, nuevo_contenido):
        self.contenido = nuevo_contenido
        print("Comentario editado.")

    def eliminar_comentario(self):
        # Implementación de eliminación
        print("Comentario eliminado.")
