import time
from random import randint
while True:
    print("Bem vindo a sua calculadora vitual:\nDigite o numero correspondente a operacao desejada\n1-Somar\n2-Multiplicar\n3-Sair")
    op=int(input())
    if op==3:
        break
    listax=[]
    listay=[]
    resultado=[]
    somalista=[]
    listamult=[]
    resultadofinal=0
    juncao=0
    cont=1
    contx=1
    conty=1
    primeiro_operando=0
    segundo_operando=0
    print("deseja que o número seja gerado aleatoriamente?(S/N)")
    resposta=str(input())
    if resposta=="n" or resposta=="N":
        print("Digite o primeiro operando: ")
        x=str(input())
        print("Digite o segundo operando: ")
        y=str(input())
        inicio=time.time()
        primeiro_operando=x
        segundo_operando=y
        listax=list(x)
        listay=list(y)
        print(op)
    elif resposta=="S" or resposta=="s":
        print("Deseja que seu primeiro operando tenha quantas casas?")
        ncasasx=int(input())
        print("Deseja que seu segundo operando tenha quantas casas?")
        ncasasy=int(input())
        inicio=time.time()
        while ncasasx>0:
            numeroaleatorio=randint(0,9)
            listax.append(numeroaleatorio)
            ncasasx-=1
        while ncasasy>0:
            numeroaleatorio=randint(0,9)
            listay.append(numeroaleatorio)
            ncasasy-=1
        tamlistax=len(listax)
        tamlistay=len(listay)
        primeiro_operando=int(listax[tamlistax-1])
        tamlistax-=1
        while tamlistax>0:
            primeiro_operando=primeiro_operando+(int(listax[tamlistax-1]*(contx*10)))        
            tamlistax-=1
            contx=contx*10
        segundo_operando=int(listay[tamlistax-1])
        tamlistay-=1
        while tamlistay>0:
            segundo_operando=segundo_operando+(int(listay[tamlistay-1]*(conty*10)))
            tamlistay-=1
            conty=conty*10
    if op==1:
        if (len(listax)==len(listay)):
            tamanho=len(listax)-1
        elif (len(listax)>len(listay)):
            while (len(listax)>len(listay)):
                listay.insert(0,'0')
        elif (len(listax)<len(listay)):
            while (len(listax)<len(listay)):
                listax.insert(0,'0')
        tamanho=len(listax)-1 
        while (tamanho>=0): 
            juncao=0
            z=(int(listax[tamanho]))+(int(listay[tamanho]))
            if z<=9:
                resultado.insert(0,z)
                tamanho-=1
            elif z>9:
                z=z-10
                juncao+=1
                tamanho-=1
                listax[tamanho]=int(listax[tamanho])+1
                int(listax[tamanho])+1
                resultado.insert(0,z)
                if tamanho==-1 and juncao>0:
                    resultado.insert(0,juncao)
        tamanhofinal=len(resultado)
        resultadofinal=int(resultado[tamanhofinal-1])
        tamanhofinal-=1
        while tamanhofinal>0:
            resultadofinal=resultadofinal+(int(resultado[tamanhofinal-1]*(cont*10)))
            tamanhofinal-=1
            cont=cont*10     
        fim = time.time()
        print("primeiro operando:",primeiro_operando)
        print("segundo operando:",segundo_operando)
        print("resposta=",resultadofinal)
        print("seu calculo foi feito em:",(fim-inicio))
    elif op==2:
        if (len(listax)==len(listay)):
            tamanho=len(listax)-1
        elif (len(listax)>len(listay)):
            while (len(listax)>len(listay)):
                listay.insert(0,'0')
        elif (len(listax)<len(listay)):
            while (len(listax)<len(listay)):
                listax.insert(0,'0')
        tamanho=len(listax)-1
        j=len(listay)-1
        while j >=0:
    
            tamanho=len(listax)-1
            while (tamanho>=0):
        
                z=(int(listax[tamanho]))*(int(listay[j])) 
                z=z+juncao
                juncao=0
                if z<=9:
                    resultado.insert(0,z)
                    tamanho-=1
                elif z>9:
                    while z>9:
                        z=z-10
                        juncao+=1
                    tamanho-=1
                    resultado.insert(0,z)
            
                    if tamanho==-1 and juncao>0:
                        resultado.insert(0,juncao)
            cont=1
            tamanhofinal=len(resultado)
            resultadofinal=int(resultado[tamanhofinal-1])
            tamanhofinal-=1
            while tamanhofinal>0:
                resultadofinal=resultadofinal+(int(resultado[tamanhofinal-1]*(cont*10)))
                tamanhofinal-=1
                cont=cont*10
            listamult.insert(0,resultadofinal)
            resultadofinal=0
            j-=1
            resultado=[]
        resultadofinal=0
        tamanholistamult=len(listamult)
    
        resultadofinal=int(listamult[tamanholistamult-1])
        contfinal=1
        tamanholistamult-=1
        while tamanholistamult>0:
            resultadofinal=resultadofinal+(int(listamult[tamanholistamult-1]*(contfinal*10)))
            tamanholistamult-=1
            contfinal*=10
        fim=time.time()
        print("primeiro operando:",primeiro_operando)
        print("segundo operando :",segundo_operando)
        print("resposta:",resultadofinal)
        print("seu calculo foi resolvido em: ",(fim-inicio))
    else:
        print("Opcao invalida!")
    print("\n---------------------------\n")