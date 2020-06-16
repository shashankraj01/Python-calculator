OPERA = ['+','-','/','*','^','R','!','logp','log','sen','cos','tg',0,'mdc', 'mmc', 'media', 'P', 'C', 'A', 'eq2']
INT = ['!','mdc', 'P', 'C', 'A']
FLOAT = ['+','-','/','*','^','R','logp','log','sen','cos','tg', 'mmc', 'media','eq2']
RESUN = ['!', 'log', 'sen', 'cos', 'tg', 'A', 'C', 'P']
b = 0

def fat(x) :
  res = math.factorial(x) ;
  return res ;

  #Clses con operaciónes


def op(x,o,y):
  if o == '+' :
    res = x + y
  elif o == '-' :
    res = x - y
  elif o == '/' :
    res = x / y
  elif o == '*' :
    res = x * y
  elif o == '^' :
    res = x ** y
  elif o == 'R' :
    res = x ** (1/y)
  elif o == '!' :
    res = fat(x)
  elif o == 'log' or op == 'logp':
    res = math.log(x,y)
  elif o == 'sen':
    res = math.sin(x)
  elif o == 'cos':
    res = math.cos(x)
  elif o == 'tg' :
    res = math.tan(x)
  elif o == 'mdc':
    res = math.gcd(x,y)
  elif o == 'mmc':
    if x != 0 or y != 0 :
      res = x * y / math.gcd(x,y)
    else :
      res = str("Error")
  elif o == 'media' :
    somatorio = 0
    i = 0
    print("Inserta un numero negativo para finalizar")
    while i != -1 :
      x = float(input('Inserta o %dº número' % (i + 1)))
      if x < 0 :
        break
      i += 1
      somatorio = somatorio + x
    res = (somatorio / i)
  elif o == 'P' :
    res = fat(x)
  elif o == 'A' :
    res = fat(x) / fat(x - y)
  elif o == 'C' :
    res = fat(x) / (fat(y) * fat(x - y))
  elif o == '1' :
    res = str("Programa Finalizado")
  elif o == 1 :
    res = str("Programa Finalizado")
  else :
    res = str("Error")
  return res

def eq(a,d,c):
  V = (d**2) - (4 * a * c)
  r1 = (-d + V**(-2)) / (2 * a)
  r2 = (-d - V**(-2)) / (2 * a)
  res = ('1ª Raiz %f\n2ª Raiz %f' % (r1,r2))
  return res

  #Escolha da operação

import math
while b in OPERA :
  #Escolher o tipo de operação
  b = input( '''\nEscoje la operación:
  + p/ Suma
  - p/ Resta
  / p/ División
  * p/ Multiplicación
  ^ p/ Potencia
  R p/ Raiz
  ! p/ Factorial
  logp p/ Algoritmo personalizado
  log p/ Algoritmo con base 10
  sen p/ Seno
  cos p/ Cosseno
  tg p/ Tangente
  mdc p/ Máximo divisor comun
  mmc p/ Mínimo multiplo comun
  media p/ Promedio de x números
  P p/ Permutación
  A p/ Arranjo
  C p/ Combinación
  eq2 p/ Equación de 2º grado
  1 p/ Cerrar
  \n''')



  #Condiciónes para canviar el texto en entrada

  if b == '+' or b == '-' or b == '/' or b == '*' :
    a = (input('Elige el primer número '))
    c = (input('Elige el segundo número '))

  elif b == '^' :
    a = (input('Elige el primer número '))
    c = (input('Elige el grado de la poténcia '))

  elif b == 'R' :
    a = (input('√'))
    c = (input('Elige el grado de la Raiz '))

  elif b == '!' :
    a = (input('Elija el número para factorizar '))
    c = (10)

  elif b == 'log':
    a = (input('Elige el primer número '))
    c = (10)

  elif b == 'logp':
    a = (input('Escoja el primer número '))
    c = (input('Elija la base de registro '))

  elif b == 'mdc' or b == 'mmc' :
    a = (input('Escoja el primer número'))
    c = (input('Elige el segundo número'))

  elif b == 'P' :
    a = (input('Cuantos elementos quieres permutar?'))
    c = 1.0

  elif b == 'A' or b == 'C' :
    a = (input('Inserta el número de elementos'))
    c = (input('Inserta el numero de elementos a agrupar'))

  elif b == 'sen' or b == 'cos' or b == 'tg' :
    a = math.radians(float(input('Escoja el valor del número (En grados)')))
    c = (10)

  elif b == 'eq2' :
    a = float(input("Inserta e valor de A"))
    d = float(input("Inserta valor de B"))
    c = float(input("Inserta valor de C"))

  else :
    a = 10.0
    c = 10.0

  #processamento do número "pi"

  if a == 'pi' :
    pi = math.pi
    a = pi
    print("Pi = ", pi)
  elif b in INT :
    a = int(a)
  elif b in FLOAT :
    a = float(a)

  if c == 'pi' :
    pi = math.pi
    c = pi
    print("Pi = ", pi)
  elif b == 'mdc':
    c = int(c)
  elif b != 'mdc' and c != 'pi' :
    c = float(c)

  #Resultados

  if b not in OPERA :
    print("Programa Finalizado")
    break

  if b == 'mmc' :
    a = int(a)
    c = int(c)

  if b not in RESUN and b != 'media' and b != 'eq2' :
    print('El resultado es\n', a, b, c, ' = %.2f' % (op(a,b,c)) )
  elif b == 'A' or b == 'C' :
    print('Total de elementos : %d\nElementos a agrupar : %d\nResultado = %d' % (a, c, op(a,b,c)))
  elif b == 'P' :
    print('Permutación de %d = %d' % (a, op(a,b,c)))
  elif b == 'media' :
    print('El resultado es\n = %.2f' % (op(a,b,c)))
  elif b in RESUN and b != '!' :
    print('El resultado es\n', b, c, ' = %.2f' % (op(a,b,c)) )
  elif b in RESUN and b == '!' :
    print('El resultado es\n', a, b, ' = %.2f' % (op(a,b,c)) )
  elif b == 'eq2' :
    print('El resultado es\n%s' % (eq(a,d,c)) )

  if b not in OPERA :
    print("Programa Finalizado")
    break
  else :
    continue
