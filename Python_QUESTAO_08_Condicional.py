lado_1 = int(input())
lado_2 = int(input())
lado_3 = int(input())

if lado_1 >=0 and lado_2 >=0 and lado_3 >=0 and (lado_1 < lado_2 + lado_3) and (lado_2 < lado_1 + lado_3) and (lado_3 < lado_2 + lado_1):
    print("É um triângulo")
else:
    print("Não é um triângulo")


