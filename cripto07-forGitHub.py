#Declaração de funções

def cifra_cesar(frase, chave, modo):
    alfabeto = 'abcdefghijklmnopqrstuvwyz àáãâéêóôõíúç@$%&*ABCDEFGHIJKLMNOPQRSTUVWYZÀÁÃÂÉÊÓÕÍÚÇ0123456789,.:?!;'
    #A nova frase recebe um texto vazio, que receberá a frase criptografada.
    nova_frase = ''
    for letra in frase:
        #irá varrer toda frase de letra em letra para identificar sua posição no alfabeto.
        indice = alfabeto.find(letra)
        #Condição que cria um looping, evitando erro de fim de indice.
        if indice == -1:
            nova_frase += letra
        else:
            novo_indice = indice + chave  if modo == mod_c else indice - chave
            #Se o modo for igual mod_c ele continua
            #Se for mod_d ele subtrai a chave para descriptografar.
            novo_indice = novo_indice % len(alfabeto)
            #a nova frase recebe letra por letra da criptografia ou descriptografia.
            nova_frase += alfabeto[novo_indice:novo_indice+1]
    return nova_frase

#Início
print('=' * 70)
logo = 'APS - Ciência da Computação - UNIP'
print(logo.center(70))
print('=' * 70)
print('\nEste é um programa que faz a encriptação e a descriptação de determinada frase!')

sair = input('\nPressione Enter para continuar. ')

#Enquanto o usuário quiser continuar, pressione enter. Para sair digita qualquer coisa.
while sair == '':
    modo = input('\nDigite C para criptografar ou D para descriptografar: ')
    #Escolha de criptografia ou descriptografia.
    if (modo == 'c') or (modo == 'C'):
        mod_c = 1
        mod_d = 0
        chave = int(input('Digite a chave: '))
        original = input('Digite uma frase: ')
        #Bloco que solicita a frase em no máximo 180 caracteres.
        while len(original) > 180:
            print('\nDigite uma frase de até 180 caracteres!')
            original = input('Digite uma frase: ')

        print('\nOriginal:', original)
        cripto = cifra_cesar(original, chave, mod_c)
        print('\nEncriptada:', cripto)
   
    else:
        mod_c = 1
        mod_d = 0
        chave = int(input('Digite a chave: '))
        original = input('Digite a frase criptografada: ')
        print('\nCriptografada:', original)
        descripto = cifra_cesar(original, chave, mod_d)
        print('\nDecriptada:', descripto)

    #retorna a função while do começo caso o usuário queira continuar.
    sair = input('\nPressione Enter para continuar ou S para sair. ')

#Fim do Programa
