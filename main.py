import re

# clientesOrdenadosHorarioTermino = sorted(cadastroAgenda, key = lambda i: i[1]['horarioTermino'])


def interval_sheduling(clientesOrdenadosHorarioTermino):

    horariovisita = -1000
    numVisita = 0

    for cliente in clientesOrdenadosHorarioTermino:
        if(horariovisita <= int(cliente[1]['horarioInicio'])):
            horariovisita = cliente[1]['horarioTermino']
            numVisita += 1
            print("cliente ", numVisita)
            print("Horário de início da visita: " + cliente[1]['horaInicio'] + ":" + cliente[1]['minutosInicio'])



def cadastra_agenda(cadastroAgenda):
    

        aux = []
        while aux == []:
            horarioInicio = input('Digite o horário inicial da visita(XX:XX): ')
            aux = re.findall("^(?:[0-1][0-9]|[2][0-3]):[0-5][0-9]$", horarioInicio)
            if aux == []:
                print('Digite um horário válido')

        
        listaHorarioInicio = horarioInicio.split(':') 
        minutosInicio = listaHorarioInicio[1]
        horaInicio = listaHorarioInicio[0]

        duracao = int(input('Digite a duração da visita: '))
        horaTermino = int(horaInicio) + int(int(duracao)/60)
        minutosTermino = int(minutosInicio) + int(duracao)%60

        if minutosTermino > 59:
            horaTermino = horaTermino + 1
            minutosTermino = minutosTermino - 60
        if horaTermino > 23:
            horaTermino = horaTermino - 24
        cliente = input('Digite o nome do cliente: ')
        email = input('Digite o email do cliente: ')
        cadastroAgenda[cliente.upper()] = {}   
        cadastroAgenda[cliente.upper()]['horaInicio'] = horaInicio
        cadastroAgenda[cliente.upper()]['minutosInicio'] = minutosInicio
        cadastroAgenda[cliente.upper()]['horarioInicio'] = int(horaInicio + minutosInicio)
        cadastroAgenda[cliente.upper()]['horaTermino'] = horaTermino
        cadastroAgenda[cliente.upper()]['minutoTermino'] = minutosTermino
        cadastroAgenda[cliente.upper()]['horarioTermino'] = int(str(horaTermino) + str(minutosTermino))
        cadastroAgenda[cliente.upper()]['duracao'] = duracao
        cadastroAgenda[cliente.upper()]['email'] = email

        print(cadastroAgenda)
        return cadastroAgenda