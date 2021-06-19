from exercicio_Python9 import Televisao
from exercicio_Python7 import Calculadora
from exercicio_Python10_contador import contadorLetras, teste

if __name__ == "__main__":
    televisao = Televisao()
    print("\n{}".format(televisao.ligada))
    televisao.power()
    print(televisao.ligada)
    televisao.aumenta_canal()
    televisao.aumenta_canal()
    print("Canal: {}".format(televisao.canal))

    calculadora = Calculadora(5,7)
    print("Soma: {}".format(calculadora.soma()))

    lista = ["cachorro", "gato", "corvo"]
    print("Nr Letras: {}".format(contadorLetras(lista)))

    print(teste())