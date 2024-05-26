#Solicite ao usuário digite o seu nome
nome_usuario = input("Digite o seu nome: ")

#Solicite ao usuário que digite o seu salário
salario_usuario = float(input("Digite o seu salário: "))

#Solicite ao usuário que digite o bonus recebido
bonus_usuario = float(input("Digite o bonus recebido: "))

CONSTANTE_BONUS = 1000

#Calcule o valor do bônus
valor_bonus = CONSTANTE_BONUS + salario_usuario * bonus_usuario

#Imprima uma mensagem para o usuário com o seu nome e o seu resultado
print(f"O usuário {nome_usuario} possui o bonus de {valor_bonus}")