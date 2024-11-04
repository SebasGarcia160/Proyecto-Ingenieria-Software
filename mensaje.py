#!/usr/bin/python
# -*- coding: utf-8 -*-

class Mensaje:
    def __init__(self, ID=None, contenido=None, emisor_id=None, receptor_id=None, fecha_envio=None):
        self.ID = ID
        self.contenido = contenido
        self.emisor_id = emisor_id
        self.receptor_id = receptor_id
        self.fecha_envio = fecha_envio

    def editar_mensaje(self, nuevo_contenido):
        self.contenido = nuevo_contenido
        print("Mensaje editado.")

    def eliminar_mensaje(self):
        # Implementación de eliminación
        print("Mensaje eliminado.")
