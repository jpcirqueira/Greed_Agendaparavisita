import cadastra_cliente
import interval_sheduling

cadastroAgenda = {}

def print_menu():
    print(30 * "-" , "MENU" , 30 * "-")
    print("1. Insere clientes a agenda")
    print("2. Mostra a lista de clientes") 
    print("3. Sair")
    print(67 * "-")
  

if __name__ == '__main__':
    loop=True
    
    while loop:
        print_menu()
        choice = input("Entre sua opcao [1-4]: ")            
        if choice=='1':
            print("Opcao 1 foi escolhida")
            cadastra_cliente.main(cadastroAgenda)    
        elif choice=='2':
            print("Opcao 2 foi escolhida")
            clientesOrdenadosHorarioTermino = sorted(cadastroAgenda.items(), key = lambda i: i[1]['horarioTermino'])            
            interval_sheduling.main(clientesOrdenadosHorarioTermino)
        elif choice=='3':
            print("Opcao 3 foi escolhida")
            print('Saindo....')
            loop=False
        else:
            input("Opcao incorreta. Aperte qualquer tecla para tentar novamente..")
