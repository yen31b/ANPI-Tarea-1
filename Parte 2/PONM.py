import math

from sympy import *
from time import time


def PONM(xo, func, tol, iterMax):
    # Aproximación de cero de la función func utilizando el método de llamado Optimal iterative algorithm with
    # four-order accuracy (PONM)
    # Estructura: [vi, xk, error, k, time] = PONM(xo, func, tol, iterMax)

    # Parámetros: xo = indica el valor donde se comienza (también representado como vi)
    # func = función a la que se le aproxima
    # tol = tolerancia de aproximación
    # iterMax = iteraciones máximas a realizar
    # xk = aproximacion del cero
    # error = error del metodo dado por | func(xk) |
    # k = iteraciones realizada

    # Guardamos el valor inicial
    vi = xo

    # Comenzamos a tomar el tiempo
    tiempo_inicial = time()

    # Tomar el string y convertirlo a una expresion que se pueda usar como funcion
    x = symbols('x')
    f = Function(func)(x)

    # Se deriva la función
    derivedSym = f.diff(x)
    # Pasamos de una expresión symbolic a una función tanto la función derivada como la función a utilizar
    # derivedf = function _handle(derivedSym)
    # func = function_handle(f)

    for k in range(iterMax):
        # Sustituir el calor de x con el de x0 en la función dericada
        derivedEvaluatedXn = derivedSym.subs(x, xo)
        # Sustituir el valor de x con el de x0 en la función original
        funcEvaluatedXn = f.subs(x, xo)
        # Obtenemos el valor de yn
        yn = xo - (funcEvaluatedXn / derivedEvaluatedXn)
        # Calculamos el valor de la función func con el valor de yn
        funcEvaluatedYn = f.subs(x, yn)
        if k == 0:
            xk = xo - ((funcEvaluatedXn * (funcEvaluatedXn - (2 * funcEvaluatedYn)) - (funcEvaluatedYn ** 2)) /
                       (derivedEvaluatedXn * (funcEvaluatedXn - 3 * funcEvaluatedYn)))
            xkMinusOne = xk
        else:
            xkMinusOne = xk
            xk = xo - ((funcEvaluatedXn * (funcEvaluatedXn - (2 * funcEvaluatedYn)) - (funcEvaluatedYn ** 2)) /
                       (derivedEvaluatedXn * (funcEvaluatedXn - 3 * funcEvaluatedYn)))
            # Después de varias pruebas se notó que xk después de ciertas iteraciones para varias funciones genera NaN,
            # entonces se decidió agregar que el momento que esto ocurra se detenga la ejecución. Aunque no se
            # determinó la causa exacta se cree que es porque los valores por ser tan similares y pequeños generan un
            # cero en el denominador causando la indefinición.
            # if math.isnan(xk):
            #     # Terminamos de contar el tiempo si se detecta una indefinición en el valor de xk
            #      tiempo_final = time() - tiempo_inicial
            #      xk = xkMinusOne
            #      break
        error = max(abs(f.subs(x, xk)), abs(xk - xkMinusOne))
        # print(lambdify(x, error, "math"))
        if error < tol:
            # Terminamos de contar el tiempo si llega al error aceptable
            tiempo_final = time() - tiempo_inicial
            break
        else:
            xo = xk
    tiempo_final = time() - tiempo_inicial
    return vi, xk, error, k, tiempo_final


x = symbols('x')
print(PONM(3, 'x**2', 1000, 9000))

