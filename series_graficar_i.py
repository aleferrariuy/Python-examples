#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Módulo: series_graficar_i.py
Descripción: Jugando con series numéricas y rep gráfica.
Autor: Alejandro
Fecha: 2025-05-06
Versión: 1.0
"""

import sys                      #para poder tomar argumentos desde la linea de comando
import os
import math                     #poderosa para operaciones matematicas
import matplotlib.pyplot as plt #para graficar, alias plt para invocar mas simple
import numpy

from datetime import datetime

x = [-5,-4,-3,-2,-1,0,1,2,3,4,5]
fx = [-5,-4,-3,-2,-1,0,1,2,3,4,5]

try:
    while True:
        plt.style.use("fivethirtyeight")
        plt.plot(
            x,
            fx,
            )
        plt.pause(0.1)
except KeyboardInterrupt:
    print("El script ",sys.argv[0]," por Usted invocado, fue ejecutado.")