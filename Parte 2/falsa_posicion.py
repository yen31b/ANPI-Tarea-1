import math
from time import time
"""
Aproximación de los ceros de la funcion utilizando el metodo de la falsa posicion
Entradas: funcion real y continua, 
         intervalo [a,b] de la funcion en el que se busca la aproximacion
         tol -> tolerancia de aproximacion
         iterMax>0 -> iteraciones maximas a realizar

Salidas: x_k -> aproximacion al cero de la funcion
        k -> numero de iteraciones realizadas
        error -> error del metodo dado por max(|funcion(x_k)|,|x_k - x_k_menos_uno|)
"""
def falsa_posicion(func, a, b, tolerancia, iter_max):
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
    if funcion(a) * funcion(b) >= 0:
        print("No se puede aplicar el metodo porque no cumple el teorema de Bolzano")
    
    # Si se cumple el teorema de Bolzano
    elif funcion(a) * funcion(b) < 0:
        for k in range(iter_max + 1):
            x_k_menos_uno = x_k
            if funcion(x_k) == 0:
                return x_k
            elif k==1:
                x_k = b - (((b-a)*funcion(b))/(funcion(b)-funcion(a)))
            else:
                x_k = b - (((b-a)*funcion(b))/(funcion(b)-funcion(a)))

            # Se verifica cual intervalo es el que cumple el teorema de Bolzano
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
falsa_posicion("0.986*x**3 - 5.181*x**2 + 9.067*x - 5.289", 1,4 ,1e-10,1000)