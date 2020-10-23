def main(clientesOrdenadosHorarioTermino):

    horariovisita = -1000
    numVisita = 0

    for cliente in clientesOrdenadosHorarioTermino:
        if(horariovisita <= int(cliente[1]['hInicioInt'])):
            horariovisita = cliente[1]['hTerminoInt']
            numVisita += 1
            print("cliente ", numVisita)
            print("Horário de início da visita: " + cliente[1]['hInicioString'] + ":" + cliente[1]['mInicioString'])