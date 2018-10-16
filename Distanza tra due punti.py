n=1
P=[]
while n<3:
    print('inserisci punto numero',n)
    raw = input('separato da virgola')
    P.append(raw.split(','))
    n += 1

dist=(((int(P[0][0])- int(P[1][0]))**2+(int(P[0][1])- int(P[1][1]))**2))**(1/2)
print(dist)



