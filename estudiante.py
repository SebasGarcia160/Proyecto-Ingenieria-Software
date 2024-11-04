#!/usr/bin/python
# -*- coding: utf-8 -*-

import usuario

class Estudiante(usuario.Usuario):
    def __init__(self, semestre=None, carrera=None, **kwargs):
        super().__init__(**kwargs)
        self.semestre = semestre
        self.carrera = carrera
