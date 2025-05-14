#Booleanos

True
False



condição = 20 > 18 #resultado é um booleano


if condição:
    print("Isso é verdade")
else:
    print("Isso é falso")


idade = int(input('Qual a sua idade? '))
cnh= input('Você tem CNH?')

if idade >= 18 and cnh == 'sim':
    print("Você pode dirigir, parabéns!")
else:
    print("Você não pode dirigir, vá jogar lol.")

condicao = idade >= 18 and cnh == 'sim'
print(condicao)

#%%
# Tabela verdade
# E = +
# OU = *
# NÃO = !
# E = and
# OU = or
# NÃO = not
print(True * 100)
print(False * 100)

print(True and True)
print(True and False)
print(False and True)
print(False and False)


print(True * True)
print(True * False)
print(False * True)
print(False * False)

print(True +  True)
print(True  + False)
print(False +  True)
print(False  + False)

print(1 * 1)
print(1 * 0)
print(0 * 1)
print(0 * 0)

print(1 * bool( 1))
print(1 * bool( 0))
print(0 * bool( 1))
print(0 * bool( 0))


print(1 + bool( 1))
print(1 + bool( 0))
print(0 + bool( 1))
print(0 +bool( 0))

