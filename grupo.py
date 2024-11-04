#!/usr/bin/python
# -*- coding: utf-8 -*-

class Grupo:
    def __init__(self, ID=None, nombre=None, descripcion=None):
        self.ID = ID
        self.nombre = nombre
        self.descripcion = descripcion

    def crear_grupo(self, nombre, descripcion):
        self.nombre = nombre
        self.descripcion = descripcion
        print("Grupo creado.")

    def unirse_grupo(self, usuario_id):
        # Lógica para unirse al grupo
        print(f"Usuario {usuario_id} se ha unido al grupo {self.nombre}.")

    def abandonar_grupo(self, usuario_id):
        # Lógica para abandonar el grupo
        print(f"Usuario {usuario_id} ha abandonado el grupo {self.nombre}.")

