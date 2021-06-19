def contadorLetras(listaPalavras):
    contador = []
    for x in listaPalavras:
        quantidade = len(x)
        contador.append(quantidade)
    return contador

def teste():
    return "teste"

if __name__ == "__main__":
    lista = ["cachorro", "gato"]
    print(contadorLetras(lista))