#https://github.com/ShingenTakeda/intro_to_hacking.git
conjunto = ['a', 'b', 'c', 'd', 'e', 'f']
senha = "bab"

def analise(lista, str, tamanhoMax):
    if(len(str) == tamanhoMax):
        if str == senha:
            print("Senha encontrada")
            print("Senha eh: " + str)
            return
            
        print(str)
        return
    
    x = len(lista)
    for i in range(0, x, 1):
        analise(lista, str + lista[i], tamanhoMax)

    return

def main():
    y = 3
    analise(conjunto, "", y)
    
main()
        