from library.interface import *
from library.funcionalidades import *
from time import sleep

palavras_novas = []
palavras_iguais = []

stop = False

while stop is not True:
    opc = menu('Analisar novo texto', 'Verificar total de palavras novas na base',
    'Verificar na base palavras que mais se repetiram', 'Sair')
    if opc == 1:
        texto = delCaracteres('Insira o texto: ')
        palavras = separadorPalavras(texto)
        palavras_novas = palavras[0]
        palavras_iguais = palavras[1]
        todas_palavras = palavras[2]
        resp = lerResposta('Deseja adicionar as palavras desse texto na base de palavras? (S/N)')
        if resp == 'S':
            basePalavras(palavras_novas, todas_palavras)
        else:
            print('Se mudar de idéia será necessário analisar o texto novamente e escolher "S"')
        titulo('resultado')
        titulo(f'Esse texto tem {len(palavras_novas)} palavra(s) nova(s):')
        exibirPalavras(palavras_novas)
        titulo(f'Esse texto tem {len(palavras_iguais)} palavra(s) repetida(s):')
        exibirPalavras(palavras_iguais)
        contPalavras(False, todas_palavras)
    elif opc == 2:
        print(totPalavras('dados/palavrasNovas.txt'))
    elif opc == 3:
        contPalavras('dados/palavrasIguais.txt')
    elif opc == 4:
        titulo('até a próxima!')
        sleep(3)
        stop = True
    else:
        print(f'Por favor, selecione uma opção válida do menu.')
