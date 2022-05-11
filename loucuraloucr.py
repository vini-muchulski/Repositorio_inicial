print("Olá, usuário(a). Bem vindo ao jogo de adivinhação")

numero_secreto = 7

chute = int(input("Digite um valor: "))

print("O valor chutado foi {}" .format(chute))

if (numero_secreto == int(chute)):
    print("Você acertou!")
else:
    if(chute > numero_secreto):
        print("Você não acertou, tente novamente! O numero chutado é maior que o mesmo designado")
    elif(chute < numero_secreto):
        print("Você não acertou, tente novamente! O numero chutado é menor que o mesmo designado")

again = input("Deseja tentar novamente? Y ou N?")
if(again == n):
    n= True
       print("Fim de jogo")




