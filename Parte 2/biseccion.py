import math
from time import time

"""
Aproximacion del cero de la funcion utilizando el metodo de la Biseccion
Entrada: funcion real y continua, 
         intervalo [a,b] de la funcion en el que se busca la aproximacion
         tol>0 -> tolerancia de aproximacion
         iterMax>0 -> iteraciones maximas a realizar

Salida: x_k -> aproximacion al cero de la funcion
        k -> numero de iteraciones realizadas
        error -> error del metodo dado por max(|funcion(x_k)|,|x_k - x_k_menos_uno|)
"""
def biseccion(func, a, b, tolerancia, iter_max):
    #Valores iniciales
    a_inicial = a
    b_inicial = b
    #Tiempo
    tiempo_inicial = time()
    #Tomar el string y convertirlo a una expresion que se pueda usar como funcion
    funcion = lambda x: eval(func)
    
    x_k = 0
    error = 0
    k = 0
    # No se puede aplicar el metodo porque no cumple las condiciones
    if funcion(a) == 0:
        x_k = a
        print("No se puede aplicar el metodo, porque f(a) = 0 entonces x_k = " + x_k)

    elif funcion(b) == 0:
        x_k = b
        print("No se puede aplicar el metodo, porque f(b) = 0 entonces x_k = " + x_k)

    elif funcion(a) * funcion(b) >= 0:
        print("No se puede aplicar el metodo porque no cumple el teorema de Bolzano")
    
    # Si se cumple el teorema de Bolzano
    elif funcion(a) * funcion(b) < 0:
        for k in range(iter_max + 1):
            x_k = (a + b) / 2
            x_k_menos_uno = x_k
            
            if funcion(x_k) == 0:
                return x_k
            
            if funcion(a) * funcion(x_k) < 0:
                b = x_k
            else:
                a = x_k
            error = max(abs(funcion(x_k)),abs(x_k - x_k_menos_uno))
            if error < tolerancia:
                break
        #parar el tiempo
        tiempo_final = time() - tiempo_inicial
        print( "valor inicial 1 = " + str(a_inicial) + "\n" + 
               "valor inicial 2 = " + str(b_inicial) + "\n" + 
               "x_k = " + str(x_k) + "\n" + 
               "error = " + str(error) + "\n" + 
               "k = " + str(k) + "\n" + 
               "tiempo(s) = " + str(tiempo_final))
        return ((a + b) / 2), error, k

#prueba   
biseccion("math.exp(x)-x-10", 2,3 ,1e-10,1000)