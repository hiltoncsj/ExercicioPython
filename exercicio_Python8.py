class Calculadora:
    def __init__(self):
        pass
    
    def soma(self, valor_a, valor_b):
        return valor_a + valor_b

    def subtracao(self, valor_a, valor_b):
        return valor_a - valor_b

    def multiplicacao(self, valor_a, valor_b):
        return valor_a * valor_b

    def divisao(self, valor_a, valor_b):
        return valor_a / valor_b

    def resto(self, valor_a, valor_b):
        return valor_a % valor_b

#instanciar uma classe
if __name__ == "__main__":
    calculadora = Calculadora()
    print("Soma: {}".format(calculadora.soma(5,3)))
    print("Subtração: {}".format(calculadora.subtracao(5,3)))
    print("Multiplicação: {}".format(calculadora.multiplicacao(5,3)))
    print("Divisão: {}".format(calculadora.divisao(5,3)))
    print("Resto: {}".format(calculadora.resto(5,3)))