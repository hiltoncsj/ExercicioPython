def escreverArquivo(texto):
    arquivo = open("texto.txt","w")
    arquivo.write(texto)
    arquivo.close()

def atualizarArquivo(texto):
    arquivo = open("texto.txt","a")
    arquivo.write(texto)
    arquivo.close()

def lerArquivo(nomeArquivo):
    arquivo = open(nomeArquivo, "r")
    texto = arquivo.read()
    print(texto)

if __name__ == "__main__":
    lerArquivo("texto.txt")