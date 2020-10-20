cadastroAgenda = [
    ('estanislau', {'horarioTermino': 1130, 'minutosInicio': '00', 'horarioInicio': 1000, 'duracao': 60, 'minutoTermino': 00, 'horaTermino': 11, 'horaInicio': '10'}),
    ('Moacir', {'horarioTermino': 1316, 'minutosInicio': '00', 'horarioInicio': 1100, 'duracao': 136, 'minutoTermino': 16, 'horaTermino': 13, 'horaInicio': '11'}),
    ('lucas siqs', {'horarioTermino': 1514, 'minutosInicio': '00', 'horarioInicio': 1200,'duracao': 60, 'minutoTermino': 14, 'ano': 1997, 'horaTermino': 15, 'horaInicio': '12'})]
 

def interval_sheduling(clientesOrdenadosHorarioTermino):
    horariovisita = -1000
    numVisita = 0

    for cliente in clientesOrdenadosHorarioTermino:
        if(horariovisita <= int(cliente[1]['horarioInicio'])):
            horariovisita = cliente[1]['horarioTermino']
            numVisita += 1
            print("cliente ", numVisita)
            print("Horário de início da visita: " + cliente[1]['horaInicio'] + ":" + cliente[1]['minutosInicio'])

interval_sheduling(cadastroAgenda)