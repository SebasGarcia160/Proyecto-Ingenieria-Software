#!/usr/bin/python
# -*- coding: utf-8 -*-

import contenido

class Publicacion(contenido.Contenido):
    def __init__(self, categoria=None, **kwargs):
        super().__init__(**kwargs)
        self.categoria = categoria

    def publicar(self):
        # Implementación de publicación
        print("Publicación realizada.")
