# %%

idade = int(input('Qual a sua idade? '))

if idade < 18:
    print("Você é menor de idade e não pode dirigir, caso insista seu pai pode ser preso.")
elif  idade > 70:
    print("Cuidado, em caso de queda pode encontrar a morte.")
else:
    print("Você é maior de idade e já pode ser preso.")
# %%

if 18<=idade<=70:
    print("Você é maior de idade e já pode ser dirigir gostosinho.")
elif idade > 70:
    print("Cuidado, em caso de queda pode encontrar a morte.")
else:
    print("Você é menor de idade vá jogar lol.")