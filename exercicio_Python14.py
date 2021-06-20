from datetime import date, time, datetime, timedelta

def datas():
    dataAtual = date.today()
    print(dataAtual.strftime("%d/%m/%Y"))

def timeAgora():
    horario = time(hour=21, minute=30, second=10)
    print(horario.strftime("%H:%M:%S"))

def dataTime():
    dataAtual = datetime.now()
    print(dataAtual.strftime("%d/%m/%Y %H:%M:%S"))
    print(dataAtual.strftime("%d/%m/%Y"))
    print(dataAtual.strftime("%H:%M:%S"))
    print(dataAtual.strftime("%c"))
    print(dataAtual.day)
    print(dataAtual.weekday())

    tupla = ("Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado", "Domingo")
    print(tupla[dataAtual.weekday()])

    dataCriada = datetime(2021, 9, 9, 8, 0, 0)
    print(dataCriada.strftime("%c"))

    dataString = "09/06/2021 20:22:10"
    dataConvertida = datetime.strptime(dataString, "%d/%m/%Y %H:%M:%S")
    print(dataConvertida)

    novaData = dataConvertida - timedelta(days=365, hours=10, minutes=30)
    print(novaData) 


if __name__ == "__main__":
    #datas()
    #timeAgora()
    dataTime()