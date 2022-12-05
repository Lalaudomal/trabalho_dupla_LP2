global f
f = 0
global restaurante
restaurante = "restaurante"
global pessoas
pessoas = "pessoas"
global periodo
periodo = {}
global tic
tic = 1234
global idreserva
idreserva = 1234

class reserva:
    def __init__(self, id, restaurante, pessoas, periodo):
        self.id = id
        self.restaurante = restaurante
        self.pessoas = pessoas
        self.periodo = periodo

def t_movie():
    global pessoas
    global f
    f = f + 1
    print("\nA reserva sera para quantas pessoas?")
    print("Digite 1 para: reserva unica")
    print("Digite 2 para: reserva para casal")
    print("Digite 3 para: reserva para +5")
    print("Digite 4 para voltar ao menu.")
    movie = int(input("Escolha a sua reserva: "))
    if movie == 1:
        pessoas = "reserva individual"
    if movie == 2:
        pessoas = "reserva casal"
    if movie == 3:
        pessoas = "reserva família"

    if movie == 4:
        center()
        theater()
        return 0
    if f == 1:
        theater()

def theater():
    global periodo
    global idreserva
    print("\nQual será o periodo da reserva? ")
    print("Digite 1 para: Diurno")
    print("Digite 2 para: Noturno")
    print("Digite 3 para: Dia todo")
    a = int(input())
    ticket = int(input("Escolha um ticket de identificação\n"))
    idreserva=ticket
    if a==1:
        periodo = "diurno"
    if a==2:
        periodo = "noturno"
    if a==3:
        periodo = "dia todo"
    timing(a)

def timing(a):
    time1 = {
        "1": "10.00 a 01.00",
        "2": "01.10 a 04.10",
        "3": "04.20 a 07.20",
        "4": "07.30 a 10.30"
    }
    time2 = {
        "1": "10.15 a 01.15",
        "2": "01.25 a 04.25",
        "3": "04.35 a 07.35",
        "4": "07.45 a 10.45"
    }
    time3 = {
        "1": "10.30 a 01.30",
        "2": "01.40 a 04.40",
        "3": "04.50 a 07.50",
        "4": "08.00 a 10.45"
    }
    if a == 1:
        print("Escolha o seu horário:")
        print("\n 1- ",time1["1"],"\n 2- ",time1["2"],"\n 3- ",time1["3"],"\n 4- ",time1["4"])
        t = input()
        x = time1[t]
        print("Sucesso! Confira os dados da sua reserva:\n-----",restaurante,"-----\nTipo da reserva:",pessoas,"\nPeríodo:",periodo,"\nHorário:",x)
    elif a == 2:
        print("Escolha o seu horário:")
        print("\n 1- ",time2["1"],"\n 2- ",time2["2"],"\n 3- ",time2["3"],"\n 4- ",time2["4"])
        t = input()
        x = time2[t]
        print("Sucesso! Confira os dados da sua reserva:\n-----",restaurante,"-----\nTipo da reserva:",pessoas,"\nPeríodo:",periodo,"\nHorário:",x)
    elif a == 3:
        print("Escolha o seu horário:")
        print("\n 1- ",time3["1"],"\n 2- ",time3["2"],"\n 3- ",time3["3"],"\n 4- ",time3["4"])
        t = input()
        x = time3[t]
        print("Sucesso! Confira os dados da sua reserva:\n-----",restaurante,"-----\nTipo da reserva:",pessoas,"\nPeríodo:",periodo,"\nHorário:",x)
    return 0

def movie(theater):
    if theater == 1:
        t_movie()
    elif theater == 2:
        t_movie()
    elif theater == 3:
        t_movie()
    elif theater == 4:
        city()
    else:
        print("Escolha errada, tente novamente.")


def center():
    print("\nEm qual ambiente será a reserva? ")
    print("1 = Interno")
    print("2 = Externo")
    print("3 = Voltar ao menu")
    a = int(input("Escolha a sua opção: "))
    movie(a)
    return 0


def city():
    global restaurante
    print("Olá, seja bem vindo: ")
    print("Em qual restaurante você deseja fazer a reserva?:\n")
    print("Digite 1 para: Restaurante América")
    print("Digite 2 para: Restaurante Ásia")
    print("Digite 3 para: Restaurante Europa")
    place = int(input("Digite a sua opção: "))
    if place == 1:
        restaurante = "Restaurante América"
        center()
    elif place == 2:
        restaurante = "Restaurante Ásia"
        center()
    elif place == 3:
        restaurante = "Restaurante Europa"
        center()
    else:
        print("Escolha errada :(")

id = idreserva
r = restaurante
p = pessoas
per = periodo
c = reserva(id,r,p,per)

city()