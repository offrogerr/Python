nome = input("Qual o seu nome? ")
sobrenome = input("Qual o seu sobrenome? ")
idade = int(input("Quantos anos voce tem? "))

ano_atual = 2026
ano_nascimento = ano_atual - idade

print(f"Ola {nome} {sobrenome}")
print(f"Voce nasceu em {ano_nascimento}")

if idade >= 18:
    print("Você é maior de idade")
else:
    print("Você é menor de idade")
    
#sobre animais
while True:
    qtde = input("Quantos animais voce tem? (0, 1, 2 ou 3) ")

    if qtde == "0":
        print("Você não tem animais")
        break
    elif qtde == "1":
        animal1 = input("Qual o nome do seu animal? ")
        print(f"Seu animal se chama {animal1}")
        break
    elif qtde == "2":
        animal1 = input("Qual o nome do primeiro animal? ")
        animal2 = input("Qual o nome do segundo animal? ")
        print(f"Seus animais se chamam {animal1} e {animal2}")
        break
    elif qtde == "3":
        animal1 = input("Qual o nome do primeiro animal? ")
        animal2 = input("Qual o nome do segundo animal? ")
        animal3 = input("Qual o nome do terceiro animal? ")
        print(f"Seus animais se chamam {animal1} e {animal2} e {animal3}")
        break
    else:
        print("Opção inválida! Tente novamente")
    
    
print("Obrigado por testar esse codigo")