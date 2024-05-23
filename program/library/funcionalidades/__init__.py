from library.interface import *

def delCaracteres(msg):
    from re import sub
    texto = str(input(msg))
    for caractere in r'–!@#$%&*(),.;:?/<>"\'1234567890_+[]{}=´|':
        texto = texto.replace(caractere, '')
    return texto.lower().split()


def separadorPalavras(texto):
    palavras_novas = []
    palavras_iguais = []
    todas_palavras = []
    for palavra in texto:
        if palavra not in palavras_novas:
            palavras_novas.append(palavra)
            todas_palavras.append(palavra)
        else:
            palavras_iguais.append(palavra)
            todas_palavras.append(palavra)
    return palavras_novas, palavras_iguais, todas_palavras


def lerResposta(msg):
    while True:
        try:
            resp = str(input(msg)).strip().upper()
        except:
            print('Tivemos um problema em ler o que você digitou. Por favor, tente novamente.')
        else:
            if resp == 'S' or resp == 'N':
                return resp
            else:
                print('Por favor: digite S ou N.')


def basePalavras(palavras_novas, todas_palavras):
    arq_pnovas = open('dados/palavrasNovas.txt', 'rt', encoding='utf-8')
    arq_piguais = open('dados/palavrasIguais.txt', 'rt', encoding='utf-8')
    lista_pnovas = arq_pnovas.read().split()
    lista_piguais = arq_piguais.read().split()
    arq_pnovas.close()
    arq_piguais.close()
    arq_pnovas = open('dados/palavrasNovas.txt', 'at', encoding='utf-8')
    arq_piguais = open('dados/palavrasIguais.txt', 'at', encoding='utf-8')
    cont_pnovas = len(lista_pnovas)
    cont_piguais = len(lista_piguais)

    qtde = 15 # qtde de palavras por linha no arquivo
    while cont_pnovas > qtde:
        cont_pnovas -= qtde
    while cont_piguais > qtde:
        cont_piguais -= qtde

    for p in palavras_novas:
        if p not in lista_pnovas:
            if cont_pnovas < qtde:
                arq_pnovas.write(f'{p} ')
            else:
                arq_pnovas.write(f'\n{p} ') # se sim, pula uma linha
                cont_pnovas = 0
            cont_pnovas += 1

    for p in todas_palavras:
        if cont_piguais < qtde:
            arq_piguais.write(f'{p} ')
        else:
            arq_piguais.write(f'\n{p} ')
            cont_piguais = 0
        cont_piguais += 1

    arq_pnovas.close()
    arq_piguais.close()


def totPalavras(arquivo):
    arquivo = open(arquivo, 'r', encoding='utf-8')
    totLista = arquivo.read().split()
    arquivo.close()
    return f'O total de palavras aprendidas até aqui foram {len(totLista)}'


def leitorInt(msg):
    try:
        num = int(input(msg))
    except:
        print('Tivemos um problema em ler sua opção. Por favor, verifique se digitou um nº inteiro.')
    else:
        return int(num)


def lerResposta(msg):
    try:
        while True:
            resp = str(input(msg)).strip().upper()
            if resp[0] in 'SN':
                break
            else:
                print('Por favor, digite "S" para sim ou "N" para não!')
    except:
        print('Tivemos um problema em ler sua resposta. Por favor, Verifique se digitou S ou N.')
    else:
        return resp[0]


def contPalavras(nome_arquivo=False, lista_palavras=False):
    if nome_arquivo != False and lista_palavras == False:
        arquivo = open(nome_arquivo, 'r', encoding='utf-8')
        lista = arquivo.read().split()
        arquivo.close()
        tit = 'palavras que mais se repetem na base'
    elif lista_palavras != False:
        lista = lista_palavras
        tit = 'palavras que mais se repetiram no texto'

    listaRepeticoes = []

    for palavra in lista:
        repeticoesPalavra = []

        for p in lista:
            if p == palavra:
                repeticoesPalavra.append(p)

        inserir = False
        dicPalavras = {}

        if len(listaRepeticoes) == 0 and len(repeticoesPalavra) > 2:
            dicPalavras['palavra'] = repeticoesPalavra[0]
            dicPalavras['quantidade'] = len(repeticoesPalavra)
            listaRepeticoes.append(dicPalavras)
        else:
            for dic in listaRepeticoes:
                if palavra in dic['palavra']:
                    inserir = False
                    break
                elif len(repeticoesPalavra) > 2:
                    inserir = True

        if inserir is True and len(listaRepeticoes) > 0:
            dicPalavras['palavra'] = repeticoesPalavra[0]
            dicPalavras['quantidade'] = len(repeticoesPalavra)
            listaRepeticoes.append(dicPalavras)

    titulo(tit)
    if len(listaRepeticoes) == 0:
        print('Não tivemos palavras que se repetiram 3 vezes ou mais.')
    else:
        c = 1
        print('obs: palavras que se repetiram menos de 3 vezes foram desconsideradas.')
        for dic in sorted(listaRepeticoes, key=lambda dic: dic['quantidade'],  reverse=True):
            print(f'{c} - {dic["palavra"].title()} - {dic["quantidade"]} vezes')
            c += 1


