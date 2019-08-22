def embelezar_down(num):
    n = list(num)
    for i in range(len(n)):
        if str(n[i]) in '13579':
            n[i] = int(n[i]) - 1
            for j in range(i+1,len(n)):
                n[j] = 8
    
    m = ''.join(str(a) for a in n)
    return int(num) - int(m)
    
def embelezar_up(num):
    n = list(num)
    for i in range(len(n)):
        if str(n[i]) in '1357':
            if n[i-1] == '8':
                z = i - 1
                while z > 0 and n[z] == '8':
                    n[z] = 0
                if z > 0:
                    n[z-1] = int(n[z-1]) + 2
            n[i] = int(n[i]) + 1
            for j in range(i+1,len(n)):
                n[j] = 0
        elif str(n[i]) == '9':
            if i > 0:
                if n[i-1] == '8':
                    z = i - 1
                    while z >= 0 and n[z] == '8':
                        n[z] = 0
                        z -= 1
                    if z >= 0:
                        n[z] = int(n[z]) + 2
                else:
                    n[i-1] = int(n[i-1]) + 2
                
                n[i] = 0
                for j in range(i+1,len(n)):
                    n[j] = 0
                    
            elif len(n) == 1:
                n[i] = 10
            
            else:
                n[i] = 0
                for j in range(i+1,len(n)):
                    n[j] = 0
                    
    if len(n) > 1:
        if n[0] == 0 and n[1] == 0:
            n = [2] + n[:]
    
    m = ''.join(str(a) for a in n)
    return int(m) - int(num)

def embelezar(n):
    m = embelezar_down(n)
    p = embelezar_up(n)
    if m > p:
        return p
    else:
        return m

testes = int(input())
dataset = []
for i in range(testes):
    dataset.append(input())

for i in range(len(dataset)):
    num = embelezar(dataset[i])
    print('Case #' + str(i+1) + ': ' + str(num))
print()
