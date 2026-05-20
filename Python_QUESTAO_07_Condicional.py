h1 = int(input())
h2 = int(input())
m1 = int(input())
m2 = int(input())

if h1 < h2:
    h1,h2 = h2,h1

if m1 < m2:
    m1,m2 = m2,m1


print("soma h mais velho + m mais nova: ", h1+m2)
print("produto h mais novo + m mais nova: ", h2*m1)
