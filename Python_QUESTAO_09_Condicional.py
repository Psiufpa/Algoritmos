a = float(input())
b = float(input())
c = float(input())

delta = b**2 - 4*a*c

if delta < 0:
    print("não existe raiz")
elif delta == 0:
    print((-b + (delta**0.5)) / (2*a), "raiz única")
else:
    print((-b + (delta**0.5)) / (2*a), "e", (-b - (delta**0.5)) / (2*a))

