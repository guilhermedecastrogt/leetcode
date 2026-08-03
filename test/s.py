numeros = [5, 12, 3, 18, 7, 2, 36, 10, 86]
maior_numero = 0
p = 0
while p<len(numeros):
    if p==0:
        maior_numero = numeros[p]
    if numeros[p]>maior_numero:
        maior_numero = numeros[p]
    p= p+1
print(maior_numero)