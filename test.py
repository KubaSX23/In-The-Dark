def giganci(liczba):
    return liczba *2

lista=[4,5,3,9,8,10,4]
gigathon=lista[3]

if gigathon >=1 or gigathon < 10:
    gigathon=gigathon+5

elif gigathon !=1 and gigathon < 10:
    gigathon=gigathon-2

elif gigathon >=5 and gigathon < 16:
    gigathon=gigathon*2

else:
    gigathon=4

for i in lista:
    gigathon=gigathon+1

i=0

while i >= 5:
    gigathon= gigathon-1
    i+=1
print(giganci(gigathon))