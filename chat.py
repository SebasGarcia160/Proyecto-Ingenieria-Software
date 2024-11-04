#!/usr/bin/python
# -*- coding: utf-8 -*-

class Chat:
    def __init__(self, ID=None, Tipo=None):
        self.ID = ID
        self.Tipo = Tipo

    def enviar_mensaje(self, contenido, receptor_id):
        # Implementación de envío de mensaje
        print(f"Mensaje enviado a {receptor_id}: {contenido}")
