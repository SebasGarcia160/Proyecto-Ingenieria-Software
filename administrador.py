#!/usr/bin/python
# -*- coding: utf-8 -*-

import usuario

class Administrador(usuario.Usuario):
    def __init__(self, permisos=None, **kwargs):
        super().__init__(**kwargs)
        self.permisos = permisos

    def gestionar_usuario(self, usuario_id):
        # Implementación de gestión de usuario
        print(f"Gestión realizada para el usuario {usuario_id}.")
