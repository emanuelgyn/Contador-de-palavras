def linha(tam=42):
    print('-'*tam)


def titulo(msg):
    linha()
    print(f'\033[1;33m{msg.upper():^42}\033[m')
    linha()


def exibirPalavras(palavras):
    c = 0
    c2 = 0
    for i, p in enumerate(palavras):
        c += 1
        c2 += 1
        if c != 5:
            if c2 != len(palavras):
                print(f'\"{p}\", ', end='')
            else:
                print(f'\"{p}\".')
        else:
            if c2 != len(palavras):
                print(f'\"{p}\", ')
            else:
                print(f'\"{p}\".')
            c = 0



def menu(*titulos):
    from library.funcionalidades import leitorInt
    titulo('contador de novas palavras')
    for i, v in enumerate(titulos):
        print(f'{i+1} - {titulos[i]}')
    linha()
    resp = leitorInt('>> ')
    return resp
