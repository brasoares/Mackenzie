import math

a = int(input("Informe o valor de a: "))
b = int(input("Informe o valor de b: "))
c = int(input("Informe o valor de c: "))

delta = (b**2)-4*(a*c)
x  = 0
x1 = 0
x2 = 0

if delta == 0:
  x = (-b+(math.sqrt(delta)))/2*a
  print("A raiz é igual a: ", x)
elif delta > 0:
  x1 = (-b+(math.sqrt(delta)))/(2*a)
  x2 = (-b-(math.sqrt(delta)))/(2*a)
  print("Através de Bháskara aplicado Δ em temos que, X1 é igual a: ", x1, "e X2 é igual a: ", x2)
else:
  print("Delta não possui raízes reais")