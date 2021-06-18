a = int(input("Entre com a primeira nota: "))
while a > 10:
    a = int(input("Nota inválida! Entre com a nota correta: "))
b = int(input("Entre com a segunda nota: "))
while b > 10:
    b = int(input("Nota inválida! Entre com a nota correta: "))
c = int(input("Entre com a terceira nota: "))
while c > 10:
    c = int(input("Nota inválida! Entre com a nota correta: "))
d = int(input("Entre com a quarta nota: "))
while d > 10:
    d = int(input("Nota inválida! Entre com a nota correta: "))
media = (a+b+c+d)/4
print("A média é: {}".format(media))
    


#a = 1
#while a <= 10:
#    print(a)
#    a += 1