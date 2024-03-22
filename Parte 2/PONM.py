import sympy as sp
import numpy as np
import time


# Función para derivadas numéricas
def derivative_numeric(f, xo, h=1e-6):
    # Incrementar el valor de h si es demasiado pequeño
    h = max(h, np.finfo(float).eps ** (1/3))
    return (f(xo + h) - f(xo)) / h


# Función principal del método PONM
def PONM(xo, func, tol, iterMax):
    # Inicialización de variables y tiempo
    vi = xo
    tiempo_inicial = time.time()
    x = sp.symbols('x')
    f = sp.sympify(func)

    # Convertir la función a una función lambda
    f_func = sp.lambdify(x, f)

    # Iteraciones del método
    for k in range(1, iterMax + 1):
        # Evaluación de la función en xo
        funcEvaluatedXn = f_func(xo)
        # Evaluación de la derivada numérica en xo
        derivedfEvaluatedXn = derivative_numeric(f_func, xo)
        # Cálculo de yn
        yn = xo - funcEvaluatedXn / derivedfEvaluatedXn
        # Evaluación de la función en yn
        funcEvaluatedYn = f_func(yn)

        # Primer paso: calcular xk y xk-1
        if k == 1:
            nominator = funcEvaluatedXn * (funcEvaluatedXn - 2 * funcEvaluatedYn) - funcEvaluatedYn ** 2
            denominator = derivedfEvaluatedXn * (funcEvaluatedXn - 3 * funcEvaluatedYn)
            xk = xo - (nominator / denominator)
            xkMinusOne = xk
        else:
            # Cálculo de xk y xk-1
            xkMinusOne = xk
            nominator = funcEvaluatedXn * (funcEvaluatedXn - 2 * funcEvaluatedYn) - funcEvaluatedYn ** 2
            denominator = derivedfEvaluatedXn * (funcEvaluatedXn - 3 * funcEvaluatedYn)
            xk = xo - (nominator / denominator)

        # Cálculo del error
        error = max(abs(f_func(xk)), abs(xk - xkMinusOne))

        # Comprobación de la tolerancia
        if error < tol:
            tiempo = time.time() - tiempo_inicial
            break
        else:
            xo = xk

    # Tiempo total de ejecución
    tiempo = time.time() - tiempo_inicial

    return vi, xk, error, k, tiempo

# Ejemplo de uso
xo = 2
func = '0.986*x**3 - 5.181*x**2 + 9.067*x - 5.289'
tol = 1e-10
iterMax = 10

vi, xk, error, k, tiempo_final = PONM(xo, func, tol, iterMax)
print("Aproximación inicial:", vi)
print("Aproximación del cero:", xk)
print("Error:", error)
print("Iteraciones realizadas:", k)
print("Tiempo total:", tiempo_final)
