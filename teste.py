import os
import re
from tkinter import filedialog as tkFileDialog
from tkinter import *
palavras_reservadas = "valor-literal,caso,faça,inteiro,ponto-flutuante"
simbolos = ["''", '""', "<", ">", "=", "=>", "<=",
            "==", "><", "<>", ";", "(", ")", "+", "-", "/", "*"]
numeros = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

opa = []
root = Tk()
teste = "1"


while(teste != "oi"):
    valint = False
    valfloat = False
    palavras_encontrada = False

    teste = int(input(
        "   \nCMD\n1)Comando \n2)Abrir arquivo (Não terminado) \n3)Limpar tela \n4)Exit \nOpção : "))
    if(teste == 1):
        comando = input("Comando:")

        if re.match('^\d+$', comando):
            valint = True
            print("\n\nNúmero INTEIRO reconhecido com sucesso !\n")
        elif re.match('^\d+\.\d+$', comando):
            valfloat = True
            print("\n\nNúmero FLOAT reconhecido com sucesso !\n")
        if((str(comando) in simbolos) == True and (valfloat == False and valint == False)):
            print("\n\nSímbolo reconhecido com sucesso !\n")
        # if((str(comando) in palavras_reservadas) == True) and (valfloat == False and valint == False):
            #print("Palavra reconhecida com sucesso !\n")
        elif(valfloat == False and valint == False and palavras_encontrada == False):
            pattern = re.compile(comando)
            x = palavras_reservadas.split(",")
            cont = len(x)
            for y in range(len(x)):
                result = pattern.match(x[y])
                if result != None:
                    if(comando.lower() in palavras_reservadas):    
                        print("\n\nPalavra reservada reconhecida com sucesso !\n")
                        palavras_encontrada = True
                if(result == None and palavras_encontrada == False):
                    cont -= 1
                    if(cont == 0):
                        print(f"\n\nPalavra {comando} não reconhecida !")
            
    if(teste == 2):
        x = ""
        f = tkFileDialog.askopenfilename()
        arq = open(f, 'r+')
        texto = arq.readlines()
        for linha in texto:
            opa.append(linha)
        arq.close()

        for q in range(len(opa)):
            x += opa[q]
        n = x.split(" ")
        print(n)
        i = palavras_reservadas.split(",")
        for k in range(i[k]):
            pattern = re.compile(i[k])
            for b in range(len(n)): 
                result = pattern.match(n[b])
            
            if result != None:
                print("\n\nValor reconhecido com sucesso !\n")
                palavras_encontrada = True
            if(result == None):
                print(f"\n\nValor {n[b]} não reconhecida !")

    if(teste == 3):
        os.system("cls")

    if(teste == 4):
        break