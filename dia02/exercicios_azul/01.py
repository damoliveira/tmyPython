#Faça um programa que vende uma garrafa de água:
#Se o cliente escolher água mineral natural, será cobrado R$1,50
#Se o cliente escolher água mineral com gás, será cobrado R$2,50

# %%

escolha = input('Você prefere Agua mineral mineral ou com gás? Ex: mineral/gas ')

if escolha == "mineral":
    print("Manda R$1,50 para cá carinha")
elif escolha == "gas":
    print("Manda R$2,50 para cá carinha")
else:
    print("Você é burro ou quer um real? É mineral ou gas")
# %%
