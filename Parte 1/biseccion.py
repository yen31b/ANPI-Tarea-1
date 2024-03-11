"""
Aproximacion del cero de la funcion utilizando el metodo de la Biseccion
Entrada: funcion real y continua, 
         intervalo [a,b]
         tol>0 -> tolerancia de aproximacion
         iterMax>0 -> iteraciones maximas a realizar
         tol = tolerancia de aproximacion

Salida: x_k -> aproximacion al cero de la funcion
        k -> numero de iteraciones realizadas
        error -> error del metodo dado por |func(xk)|
"""
def biseccion(funcion, a, b, tolerancia, iter_max):
    x_k = 0
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
            x_k_menos_uno = xk
            
            if f(x_k) == 0:
                return x_k
            
            if f(a) * f(x_k) < 0:
                b = x_k
            else:
                a = x_k
        return (a + b) / 2
        
        error = max(abs(funcion(x_k)),abs(x_k - x_k_menos_uno))
        if error < tolerancia:
            break
    print( "x_k = " + x_k + "\n" + "error = " + error + "\n" + "k = " + k)
    return x_k,error,k
   

"""
function [xk,error,k]=biseccion(a,b,func,tol,iterMax)
  %
  % Aproximacion del cero de la funcion func utilizando el metodo de la Biseccion
  %
  % Estructura: [xk,error,k]=biseccion(a,b,func,tol,iterMax)
  %
  % Parametros: a,b = intervalo [a,b] donde se busca el cero
  %             func = texto que representa a la funcion a la que se le aproxima el cero
  %             tol = tolerancia de aproximacion
  %             iterMax = iteraciones maximas a realizar
  %             xk = aproximacion del cero
  %             error = error del metodo dado por |func(xk)|
  %             k = iteraciones realizadas
  %
  % [xk,error,k]=biseccion(2,3,'exp(x)-x-10',1e-10,1000)


  % Texto a una Funcion Numerica en Octave
  f=str2func(['@(x)' func]);

  if f(a)*f(b)<0
    for k=1:iterMax
      xk=(a+b)/2;
      if f(a)*f(xk)<0
        b=xk;
      else
        a=xk;
      end
      error=abs(f(xk));
      if error<tol
        break
      end
    end
  else
    xk='N/A';
    error='N/A';
    k='N/A';
    display('No se cumple la condicion de Bolzano con los datos dados')
  end

end
"""