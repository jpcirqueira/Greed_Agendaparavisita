import re

def main(cadastroAgenda):
        aux = []
        while aux == []:
            hInicioInt = input('Digite o horário inicial da visita(XX:XX): ')
            aux = re.findall("^(?:[0-1][0-9]|[2][0-3]):[0-5][0-9]$", hInicioInt)
            if aux == []:
                print('Digite um horário válido')

        
        listaHorarioInicio = hInicioInt.split(':') 
        mInicioString = listaHorarioInicio[1]
        hInicioString = listaHorarioInicio[0]

        cliente = input('Digite o nome do cliente: ')
        email = input('Digite o email do cliente: ')
        wpp = input('Digite seu número de whatsapp Ex: 61992847289: ')
        visitaDuracao = int(input('Digite a duração da visita em minutos: '))

        hTerminoInt = int(hInicioString) + int(int(visitaDuracao)/60)
        mTerminoInt = int(mInicioString) + int(visitaDuracao)%60

        if mTerminoInt > 59:
            hTerminoInt = hTerminoInt + 1
            mTerminoInt = mTerminoInt - 60
        if hTerminoInt > 23:
            hTerminoInt = hTerminoInt - 24

        cadastroAgenda[cliente.upper()] = {}
        cadastroAgenda[cliente.upper()]['visitaDuracao'] = visitaDuracao
        cadastroAgenda[cliente.upper()]['hInicioString'] = hInicioString
        cadastroAgenda[cliente.upper()]['mInicioString'] = mInicioString
        cadastroAgenda[cliente.upper()]['hInicioInt'] = int(hInicioString + mInicioString)
        cadastroAgenda[cliente.upper()]['mTerminoInt'] = mTerminoInt
        cadastroAgenda[cliente.upper()]['hTerminoInt'] = int(str(hTerminoInt) + str(mTerminoInt))
        cadastroAgenda[cliente.upper()]['hTermino'] = hTerminoInt
        cadastroAgenda[cliente.upper()]['email'] = email
        cadastroAgenda[cliente.upper()]['wpp'] = wpp
        return cadastroAgenda
