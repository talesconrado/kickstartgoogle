testes = int(input())
dataset = []
for i in range(testes):
    dataset.append(input())


def bonito(numero):
    """Avalia se o número é "bonito", ou seja, tem apenas caracteres pares"""
    numero = str(numero)
    for i in range(len(numero)):
        if int(numero[i]) % 2 == 0:
            pass
        else:
            return False
    return True

def onde_esta_feio(numero):
    """Testa os números até achar um "feio", ao achar, guarda sua posição, se não acha nenhum, retorna -1"""
    numero = str(numero)
    for i in range(len(numero)):
        if bonito(numero[i]):
            pass
        else:
            return i
            break
    return -1


def embelezar_up(numero):
    """Deixa o número com a configuração "bonita" mais próxima para cima, aumentando o primeiro ímpar 
    e colocando zeros no resto"""
    if onde_esta_feio(numero) == -1:
        return 0
    else:
        lista = [int(x) for x in str(numero)]
        partida = onde_esta_feio(numero)
        
        lista[partida] += 1
        
        for i in range(partida+1,len(lista)):
            lista[i] = 0
        resposta = ''.join(str(x) for x in lista)
        distancia = abs(int(numero) - int(resposta))
        return distancia

def embelezar_down(numero):
    """Deixa o número com a configuração "bonita" mais próxima para baixo, diminuindo o primeiro ímpar 
    e colocando oitos no resto"""
    if onde_esta_feio(numero) == -1:
        return 0
    else:
        lista = [int(x) for x in str(numero)]
        partida = onde_esta_feio(numero)
        lista[partida] -= 1
        for i in range(partida+1, len(lista)):
            lista[i] = 8   
        resposta = ''.join(str(x) for x in lista)
        distancia = abs(int(numero) - int(resposta))
        return distancia

def mais_proximo(numero):
    """Simplesmente compara e pega o menor entre os "embelezamentos""""
    if embelezar_up(numero) > embelezar_down(numero):
        return embelezar_down(numero)
    else:
        return embelezar_up(numero)      


for i in range(len(dataset)):
    num = mais_proximo(dataset[i])
    print('Case #' + str(i+1) + ': ' + str(num))
