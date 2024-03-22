import math
from time import time
from sympy import *
import numpy as np

#van_der_waals = 1 - ((16/7)*sqrt(x)) + ((4/3)*x) - ((1/21)*x^4)

# Funcion de Van der Waals
#van_der_waals = "0.986*x**3 - 5.181*x**2 + 9.067*x - 5.289"

def van_der_waals(x):
  func = 0.986*x**3 - 5.181*x**2 + 9.067*x - 5.289
  return func
"""
Funcion y_n del metodo de KJNM: calcula el valor de y_n necesario en el metodo de KJNM
Entradas: x_n -> funcion x sub n del metodo
Salidas: y_n -> funcion y sub n del metodo
"""
def funcion_y_n(x_n):    
    numerador = van_der_waals(x_n)
    # Derivada de la funcion de Van der Waals
    denominador = van_der_waals(x_n).diff(x_n)
    # Se indefine la funcion = diverge (infinito)
    if denominador == 0:
      y_n = -math.inf
      print("Funcion diverge a -infinito")
    else:
      y_n = x_n - (numerador/denominador)
    return y_n

"""
Funcion x_n_mas_uno del metodo de KJNM: calcula el valor de y_n necesario en el metodo de KJNM
Entradas: 
        x_n -> funcion x sub n del metodo
        y_n -> funcion y sub n del metodo
Salidas:
        Valor de la funcion x sub n+1 del metodo
"""
def funcion_x_n_mas_uno(x_n, y_n):    
    numerador = van_der_waals(x_n)^2 + van_der_waals(y_n)^2
    denominador = van_der_waals.diff(x_n)*(van_der_waals(x_n)- van_der_waals(y_n))
    # Se indefine la funcion = diverge (infinito)
    if denominador == 0:
      x_n_mas_uno = -math.inf
      print("Funcion diverge a -infinito")
    else:
      x_n_mas_uno = x_n - (numerador/denominador)
    return x_n_mas_uno

def KJNM(func_y_n,func_x_n_mas_uno, valor_inicial, tolerancia, iter_max):
    #Tiempo
    tiempo_inicial = time()
    # Guardar valor inicial
    vi = valor_inicial
    x = valor_inicial

    funcion_vdw = lambda x: eval(van_der_waals)
    #Inicializar valores que devuelve el metodo
    x_k = 0
    error = 0
    k = 0
    
    for k in range(iter_max + 1):
        y_n = funcion_y_n(x)
        x_n_mas_uno = funcion_x_n_mas_uno(x, y_n)
        x_menos_1 = x
        error = max(abs(funcion_vdw(x)),abs(x-(x_menos_1)))
        if error < tolerancia:
          break
        else:
          x = x_n_mas_uno
    x_k = x
    #parar el tiempo
    tiempo_final = time() - tiempo_inicial
    print( "valor inicial (v.i) = " + str(vi) + "\n" +
            "x_k = " + str(x_k) + "\n" + 
            "error = " + str(error) + "\n" + 
            "k = " + str(k) + "\n" + 
            "tiempo(s) = " + str(tiempo_final))
    return x_k, error, k

#prueba   
KJNM( lambda x_n: funcion_y_n(x_n), lambda x_n, y_n: funcion_x_n_mas_uno(x_n, y_n), 1 , 1e-10, 100)