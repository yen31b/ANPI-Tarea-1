"""
Aproximación de cero de la función func utilizando el método de la falsa posición
  
Estructura: [vi1,vi2,xk,error,k,time] = falsaPosicion(a,b,func,tol,iterMax)
  
Parámetros: a,b = intervalo [a,b] donde se busca el cero (también representados como vi1 y vi2)
              func = función a la que se le aproximación
              tol = tolerancia de aproximación
              iterMax = iteraciones máximas a realizar
              xk = aproximacion del cero
              error = error del metodo dado por |func(xk)|
              k = iteraciones realizada
  
[vi1,vi2,xk,error,k,time]=falsaPosicion(0.75,1.05,'1-(16*sqrt(x)/7)+(4*x/3)-(1*(x^4)/21)',1e-10,1000)
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
    return