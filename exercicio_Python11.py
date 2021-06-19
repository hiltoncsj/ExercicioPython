contadorLetras = lambda lista: [len(x) for x in lista]
lista = ["cachorro", "gato", "corvo"]
print("Letras: {}".format(contadorLetras(lista)))

soma = lambda a, b : a + b
print("Soma: {}".format(soma(5,10)))

calculadora = {
    "soma": lambda a, b : a + b,
    "subtracao": lambda a, b : a - b,
    "multiplicacao": lambda a, b : a * b,
    "divisao": lambda a, b : a / b
}

soma = calculadora["soma"]
print("Soma lambda: {}".format(soma(10,5)))