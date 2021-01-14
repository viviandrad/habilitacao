print("*********************************")
print("Você sabe se pode tirar a habilitação?")
print("*********************************")

idade_habilitacao = 18

inserir_idade_str = input("Digite a sua idade: ")

print ("Você digitou ", inserir_idade_str)

inserir_sua_idade = int(inserir_idade_str)
idade_igual = idade_habilitacao == inserir_sua_idade
idade_maior = idade_habilitacao < inserir_sua_idade
idade_menor = idade_habilitacao > inserir_sua_idade

if (idade_igual):
    print ("Você pode tirar a habilitação!")
else:
    if (idade_maior):
        print("Você pode tirar a habilitação!")
    elif (idade_menor):
        print("Você não pode tirar a habilitação!")

print("Fim")