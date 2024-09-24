'''
1 - Incluir o índice do elemento na mensagem. ✔️
2 - Fazer com que o sistema pergunte ao usuário o nome que ele deseja procurar. ✔️
3 - Continuar perguntando até achar o nome. ✔️
'''

def achar_nome(elemento, lista):
  achou = False

  for i in range(len(lista)):
    if lista[i] == elemento:
      achou = True

  if(achou == False):
    print("Não achamos o nome: " + elemento)
  else:
    index = lista.index(elemento)
    print("Achamos o nome: {}, na posição: {}".format(elemento, index + 1))
#end def

def procurar_nome(lista):
  while True:
    nome = input("Digite o nome que deseja procurar: ")

    achar_nome(nome, lista)

    if nome in lista:
      break
    else :
      print("Tente novamente.\n")
#end def

nomes = ["Ana", "Graziele", "Paulo", "Marcio"]

procurar_nome(nomes)