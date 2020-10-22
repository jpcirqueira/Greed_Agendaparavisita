import re

def main(cadastroAgenda):
        aux = []
        while aux == []:
            horarioInicio = input('Digite o horário inicial da visita(XX:XX): ')
            aux = re.findall("^(?:[0-1][0-9]|[2][0-3]):[0-5][0-9]$", horarioInicio)
            if aux == []:
                print('Digite um horário válido')

        
        listaHorarioInicio = horarioInicio.split(':') 
        minutosInicio = listaHorarioInicio[1]
        horaInicio = listaHorarioInicio[0]

        cliente = input('Digite o nome do cliente: ')
        email = input('Digite o email do cliente: ')
        wpp = input('Digite seu número de whatsapp Ex: 61992847289: ')
        duracao = int(input('Digite a duração da visita em minutos: '))

        horaTermino = int(horaInicio) + int(int(duracao)/60)
        minutosTermino = int(minutosInicio) + int(duracao)%60

        if minutosTermino > 59:
            horaTermino = horaTermino + 1
            minutosTermino = minutosTermino - 60
        if horaTermino > 23:
            horaTermino = horaTermino - 24

        cadastroAgenda[cliente.upper()] = {}
        cadastroAgenda[cliente.upper()]['duracao'] = duracao
        cadastroAgenda[cliente.upper()]['horaInicio'] = horaInicio
        cadastroAgenda[cliente.upper()]['minutosInicio'] = minutosInicio
        cadastroAgenda[cliente.upper()]['horarioInicio'] = int(horaInicio + minutosInicio)
        cadastroAgenda[cliente.upper()]['minutoTermino'] = minutosTermino
        cadastroAgenda[cliente.upper()]['horarioTermino'] = int(str(horaTermino) + str(minutosTermino))
        cadastroAgenda[cliente.upper()]['horaTermino'] = horaTermino
        cadastroAgenda[cliente.upper()]['email'] = email
        cadastroAgenda[cliente.upper()]['wpp'] = wpp
        return cadastroAgenda
