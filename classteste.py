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

id=idreserva
r=restaurante
p=pessoas
per=periodo
c = reserva(id,r,p,per)

print(c.id,c.restaurante)