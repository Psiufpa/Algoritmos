valor = float(input())

total = 0
dia = 0

while dia != -1:

    dia = int(input())
    categoria = input()

    if 6<=dia<=13:
        
        if categoria =="E":
            total += valor*0.8
        else:
            total += valor*0.9
    
    elif 13<dia<=31:
    
        if categoria =="E":
            total += valor*0.9
        else:
            total += valor*0.95

print (total)
