'''
Copie o array apresentado embaixo no seu editor de código, e imprima no terminal: a
quantidade de elementos que ele possui, o dado salvo no índice 2, o dado salvo no índice
9, e dado salvo no índice 14.

lista_musicos = ['Djavan', 'Roberto Carlos', 'Elis Regina', 'Tom Jobim', 'Milton Nascimento', 'Chico Buarque', 'Nara Leão', 'Pitty', 'Simonal', 'Moacir Santos', 'Caetano Veloso', 'Elza Soares', 'Paulinho da Viola', 'Yamandú Costa', 'Gal Costa'] 
'''

lista_musicos: list[str] = ['Djavan', 'Roberto Carlos', 'Elis Regina', 'Tom Jobim', 'Milton Nascimento', 'Chico Buarque', 'Nara Leão', 'Pitty', 'Simonal', 'Moacir Santos', 'Caetano Veloso', 'Elza Soares', 'Paulinho da Viola', 'Yamandú Costa', 'Gal Costa']

print("Quantidade de elementos que o array lista_musicos possui: ", len(lista_musicos))
print("Dado salvo no índice 2: ", lista_musicos[2])
print("Dado salvo no índice 9: ", lista_musicos[9])
print("Dado salvo no índice 14", lista_musicos[14])
