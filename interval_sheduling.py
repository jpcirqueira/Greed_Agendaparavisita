def main(clientesOrdenadosHorarioTermino):

    horariovisita = -1000
    numVisita = 0
    confirmados = []
    # print(clientesOrdenadosHorarioTermino)
    print(clientesOrdenadosHorarioTermino)
    for cliente in clientesOrdenadosHorarioTermino:
        if(horariovisita <= int(cliente[1]['hInicioInt'])):
            horariovisita = cliente[1]['hTerminoInt']
            numVisita += 1
            confirmados.append(cliente[1]['email'])
            print("cliente ", numVisita)
            print(cliente[0])
            print("Horário de início da visita: " + cliente[1]['hInicioString'] + ":" + cliente[1]['mInicioString'])


    return confirmados