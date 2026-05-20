n = int(input())

saida = ""
for i in range (n):
    if i % 2 == 0:
        saida = saida + "@"
        print (saida)
    else:
        saida = saida + "#"
        print (saida)

