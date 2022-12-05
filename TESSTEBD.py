import sqlite3
import pandas as pd
from sqlite3 import Error
def criabd(listareservas):

    banco = sqlite3.connect('BDteste.db')
    c = banco.cursor()
    c.execute("CREATE TABLE Reservas (ID integer, Restaurante text, Tipo text, Periodo text,Horario text")
    for i in listareservas.columns:
        listareservas.to_sql('Reservas',if_exists='replace',index=False)