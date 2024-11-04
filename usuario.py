#!/usr/bin/python
# -*- coding: utf-8 -*-

class Usuario:
    def __init__(self, ID=None, correo_electronico=None, contraseña_encriptada=None, nombre=None, apellido=None, fecha_nacimiento=None, notificaciones_activas=None):
        self.ID = ID
        self.correo_electronico = correo_electronico
        self.contraseña_encriptada = contraseña_encriptada
        self.nombre = nombre
        self.apellido = apellido
        self.fecha_nacimiento = fecha_nacimiento
        self.notificaciones_activas = notificaciones_activas
