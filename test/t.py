#primeiro definir um numero secreto
#depois pedir um numero
#while nao acertar 
#if o numero  for menor print (muito baixo tente dnv) 
#peca o numero dnv
#if o numero for maior print (muito alto tente dnv)
#peca o numero dnv
#if o numero for certo print (parabens voce acertou)

n = 0
s = 5 
print ("tentativa: ", n)
x = int(input("digite um numero: ")) 
while x != s:
    if x < s: 
        n = n+1
        print ("muito baixo try again")
        print ("tentativa: ", n) 
        x = int(input("digite um numero: "))
       

    if x > s:
        n = n+1
        print ("muito alto try again")
        print ("tentativa: ", n) 
        x = int(input("digite um numero: "))
       
    if x == s:
        print ("congrats") 
        print ("concluido em: ", n," vezes ")  
 







