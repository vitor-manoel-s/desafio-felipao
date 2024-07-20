# Crie uma variável para armazenar o nome e a quantidade de experiência (XP) de um herói
nome = "Vitor"
xpHeroi = 8000

if xpHeroi < 1000:   # Se XP for menor do que 1000 = Ferro.
    nivel = "Ferro"
elif xpHeroi < 2001: # Se XP for entre 1001 e 2000 = Bronze.
    nivel = "Bronze"
elif xpHeroi < 5001: # Se XP for entre 2001 e 5000 = Prata.
    nivel = "Prata"
elif xpHeroi < 7001: # Se XP for entre 5001 e 7000 = Ouro.
    nivel = "Ouro"
elif xpHeroi < 8001: # Se XP for entre 7001 e 8000 = Platina.
    nivel = "Platina"
elif xpHeroi < 9001: # Se XP for entre 8001 e 9000 = Ascendente.
    nivel = "Ascendente"
elif xpHeroi< 10001: # Se XP for entre 9001 e 10000 = Imortal.
    nivel = "Imortal"
else:                # Se XP for maior ou igual a 10001 = Radiante.
    nivel = "Radiante"

# Saída
print("O Herói {0} está no nível {1}.".format(nome,nivel))