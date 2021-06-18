a = int(input("Entre com o 1 valor: "))
b = int(input("Entre com o 2 valor: "))
soma = a+b
subtracao = a-b
multiplicacao = a*b
divisao = a/b
resto = a%b
print('Soma: {soma}'
'\nSubtração: {subtracao}'
'\nMultiplicação: {multiplicacao}'
'\nDivisão: {divisao}'
'\nResto: {resto}'
.format(soma=soma, 
        subtracao=subtracao, 
        multiplicacao=multiplicacao, 
        divisao=divisao,
        resto=resto))