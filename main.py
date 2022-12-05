import pandas as pd
from numpy import random
import sqlite3
global t1
t1 = False
global t2
t2 = False
global t3
t3 = False
global t4
t4 = False
from sqlite3 import Error
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
global listareservas
listareservas = pd.DataFrame()
global tempo
import matplotlib.pyplot as grafico
class reserva:
    def _init_(self, id, restaurante, pessoas, periodo):
        self.id = id
        self.restaurante = restaurante
        self.pessoas = pessoas
        self.periodo = periodo

def t_reserva():
    global pessoas
    global f
    f = f + 1
    print("\nA reserva sera para quantas pessoas?")
    print("Digite 1 para: reserva unica")
    print("Digite 2 para: reserva para casal")
    print("Digite 3 para: reserva para 3 ou mais")
    print("Digite 4 para voltar ao menu.")
    treserva = int(input("Escolha a sua reserva: "))
    if treserva == 1:
        pessoas = "Individual"
        theater()
    if treserva == 2:
        pessoas = "Casal"
        theater()
    if treserva == 3:
        pessoas = "Família"
        theater()

    if treserva > 3:
        #center()
        #theater()
        return 0
    #if f == 1:
    #    theater()

def theater():
    global t4
    global periodo
    global idreserva
    print("\nQual será o periodo da reserva? ")
    print("Digite 1 para: Diurno")
    print("Digite 2 para: Noturno")
    print("Digite 3 para: Dia e Noite")
    a = int(input())
    idreserva=random.randint(1000)
    if a==1:
        periodo = "Diurno"
        t4=True
    if a==2:
        periodo = "Noturno"
        t4=True
    if a==3:
        periodo = "Dia e Noite"
        t4=True
    if a<1 or a>3:
        print("Escolha errada :(")
        t4=False
    timing(a)

def timing(a):
    global tempo
    global t3
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
        #global tempo
        print("Escolha o seu horário:")
        print("\n 1- ",time1["1"],"\n 2- ",time1["2"],"\n 3- ",time1["3"],"\n 4- ",time1["4"])
        t = int(input())
        if t < 1 or t > 4:
            print("Escolha errada :(")
            t3 = False
            return 0
        t3 = True
        x = time1[str(t)]
        tempo = x
        print("Sucesso! Confira os dados da sua reserva:\n-----",restaurante,"-----\nTipo da reserva:",pessoas,"\nPeríodo:",periodo,"\nHorário:",x)
    elif a == 2:
        #global tempo
        print("Escolha o seu horário:")
        print("\n 1- ",time2["1"],"\n 2- ",time2["2"],"\n 3- ",time2["3"],"\n 4- ",time2["4"])
        t = int(input())
        if t < 1 or t > 4:
            print("Escolha errada :(")
            t3 = False
            return 0
        else:
            x = time2[str(t)]
            tempo = x
            t3 = True
            print("Sucesso! Confira os dados da sua reserva:\n-----",restaurante,"-----\nTipo da reserva:",pessoas,"\nPeríodo:",periodo,"\nHorário:",x)
    elif a == 3:
        #global tempo
        print("Escolha o seu horário:")
        print("\n 1- ",time3["1"],"\n 2- ",time3["2"],"\n 3- ",time3["3"],"\n 4- ",time3["4"])
        t = int(input())
        if t < 1 or t > 4:
            print("Escolha errada :(")
            t3 = False
            return 0
        t3=True
        x = time3[str(t)]
        tempo = x
        print("Sucesso! Confira os dados da sua reserva:\n-----",restaurante,"-----\nTipo da reserva:",pessoas,"\nPeríodo:",periodo,"\nHorário:",x)
    return 0

def reservat(theater):
    global t2
    if theater == 1:
        t_reserva()
        t2=True
    elif theater == 2:
        t_reserva()
        t2=True
    elif theater == 3:
        t_reserva()
        t2=True
    else:
        print("Escolha errada :(")
        t2=False
        return

x = [9,8,3,4]
def center():
    print("\nEm qual ambiente será a reserva? ")
    print("1 = Interno")
    print("2 = Externo")
    print("3 = Voltar ao menu")
    a = int(input("Escolha a sua opção: "))
    reservat(a)
    return 0

y = [9,5,3,4]
def city():
    global restaurante
    global t1
    print("\n-------------------\nOlá, seja bem vindo!")
    print("Em qual restaurante você deseja fazer a reserva?:\n")
    print("Digite 1 para: Restaurante América")
    print("Digite 2 para: Restaurante Ásia")
    print("Digite 3 para: Restaurante Europa")
    place = int(input("Digite a sua opção: "))
    if place == 1:
        restaurante = "Restaurante América"
        center()
        t1=True
    elif place == 2:
        restaurante = "Restaurante Ásia"
        center()
        t1=True
    elif place == 3:
        restaurante = "Restaurante Europa"
        center()
        t1=True
    else:
        print("Escolha errada :(")
        t1=False
        return

def trava():
    travaloop = input(str("Gostaria de fazer mais uma reserva?\n 1 - S   |   2 - N\n"))
    if travaloop.upper()=="N":
        return False;
    else: return True;

i=0
idlist=[]
restaurantelist=[]
pessoaslist=[]
periodolist=[]
tempolist=[]


def criabd(listareservas):

    con = sqlite3.connect('BDteste.db')
    c = con.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS Reservas111 (ID integer, Restaurante text, Tipo text, Periodo text,Horario text)")
    #Usando o método .to_sql transformamos a tabela de reservas (objeto pandas) para sql, com a condição
    #de que, caso a tabela já esteja criada, os valores do novo dataframe listareservas (capturados
    #por cada execução do código) serão escritos.
    listareservas.to_sql('Reservas',con,if_exists='append',index=False)
    con.commit()
    c.execute('''  
    SELECT * FROM Reservas
              ''')
    for row in c.fetchall():
        print(row)

while True:
    city()
    if t1==False or t2==False or t3==False or t4==False:
        continue
    id = idreserva
    r = restaurante
    p = pessoas
    per = periodo
    tem = tempo
    idlist.append(id)
    restaurantelist.append(r)
    pessoaslist.append(p)
    periodolist.append(per)
    tempolist.append(tempo)
    i+=1
    if trava()==False:
        listareservas["ID"] = idlist
        listareservas["Restaurante"] = restaurantelist
        listareservas["Tipo"] = pessoaslist
        listareservas["Período"] = periodolist
        listareservas["Horário"] = tempolist
        print("\n----- As reservas feitas nessa execução foram: -----\n",listareservas)
        print("\n----- As reservas totais são: -----\n")
        criabd(listareservas)
        break



grafico.ylabel('volume de pessoas')
grafico.xlabel('periodo do dia')
grafico.bar(x,y )
grafico.show()