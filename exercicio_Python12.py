import shutil

def escreverArquivo(texto):
    arquivo = open("C:/DEV/Python/textos/texto.txt","w")
    arquivo.write(texto)
    arquivo.close()

def atualizarArquivo(texto):
    diretorio = "C:/DEV/Python/textos/texto.txt"
    arquivo = open(diretorio,"a")
    arquivo.write(texto)
    arquivo.close()

def lerArquivo(nomeArquivo):
    arquivo = open(nomeArquivo, "r")
    texto = arquivo.read()
    print(texto)

def copiaArquivo(nomeArquivo):
    shutil.copy(nomeArquivo, "C:/DEV/Python/textos/")

def moveArquivo(nomeArquivo):
    shutil.move(nomeArquivo, "C:/DEV/Python/textos/")

if __name__ == "__main__":
    #moveArquivo("texto.txt")