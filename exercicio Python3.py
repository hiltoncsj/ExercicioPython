#Mostrar os números primos até o número digitado
a = int(input("Entre com um número: "))
for x in range(a+1):
    div = 0
    for y in range(1, x+1):
        resto = x % y
        if resto == 0:
            div += 1
    if div == 2:
        print(y)

#Ver se o número digitado é primo
#a = int(input("Entre com um número: "))
#div = 0
#
#for x in range(1,a+1):
#    resto = a % x
#    if resto == 0:
#        div += 1
#
#if div == 2:
#    print("Esse número é primo")
#else:
#    print("Esse número não é primo")