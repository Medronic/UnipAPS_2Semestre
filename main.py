import base64
import time
print("Bem-vindo ao projeto da APS! Sobre: Criptografia.")

def mensagem_predefinida():
    mensagem_predefinida = 'Essa é a "encriptacão" gerada utilizando Base64'
    message_bytes = mensagem_predefinida.encode('utf-8')
    base64_bytes = base64.b64encode(message_bytes)
    base64_message = base64_bytes.decode('utf-8')

    print("Texto Encriptado:", base64_message)

    base64_message = base64_message
    base64_bytes = base64_message.encode('utf-8')
    message_bytes = base64.b64decode(base64_bytes)
    mensagem_predefinida = message_bytes.decode('utf-8')

    print("Texto Desencriptado:", mensagem_predefinida)

    opcao = int(input('''Deseja voltar ao Menu principal?
    1 - Sim.
    2 - Não.
    Digite: '''))
    if opcao == 1:
        print("-------------------------------------")
        menu()
    elif opcao == 2:
        print("-------------------------------------")
        print("Saindo em 3...")
        time.sleep(1)
        print("Saindo em 2..")
        time.sleep(1)
        print("Saindo em 1.")
        time.sleep(1)
        print("Até mais!")
    else:
        print("Opcão inexistente!\n Tente novamente:")
        print("-------------------------------------")
        menu()

def mensagem_customizada():
    sua_mensagem = str(input("Digite a mensagem a ser codificada: "))
    message_bytes = sua_mensagem.encode('utf-8')
    base64_bytes = base64.b64encode(message_bytes)
    base64_message = base64_bytes.decode('utf-8')

    print("Você digitou a mensagem:",sua_mensagem,", ela foi codificada e passou a ser:", base64_message)
    print("-------------------------------------")
    opcao = int(input('''Deseja voltar ao Menu principal?
    1 - Sim.
    2 - Não.
    Digite: '''))
    if opcao == 1:
        print("-------------------------------------")
        menu()
    elif opcao == 2:
        print("Saindo em 3...")
        time.sleep(1)
        print("Saindo em 2..")
        time.sleep(1)
        print("Saindo em 1.")
        time.sleep(1)
        print("Até mais!")
    else:
        print("Opcão inexistente!\n Tente novamente:")
        print("-------------------------------------")
        menu()

def menu():
    opcao = int(input('''Menu:
    1 - Mensagem Predefinida.
    2 - Mensagem Customizada.
    3 - Creditos
    4 - Fechar Programa
    Digite: '''))
    if opcao == 1:
        print("-------------------------------------")
        mensagem_predefinida()
    elif opcao == 2:
        print("-------------------------------------")
        mensagem_customizada()
    elif opcao == 3:
        print('''
        Programa criado por Moisés Freitas
                    RA: F1610J2,
        Integrantes: 
        ''')
    elif opcao == 4:
        print("-------------------------------------")
        print("Saindo em 3...")
        time.sleep(1)
        print("Saindo em 2..")
        time.sleep(1)
        print("Saindo em 1.")
        time.sleep(1)
        print("Até mais!")
    else:
        print("-------------------------------------")
        print("Opcão inexistente!\n Tente novamente:")
        print("-------------------------------------")
        menu()

menu()
