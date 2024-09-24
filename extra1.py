'''
Boa tarde,

Estamos modernizando nossa loja e precisamos de um novo sistema de controle de estoque. Geralmente anotamos todos os produtos que temos disponíveis, e quando um dos produtos acaba, substituímos ele por algum outro produto.

Ouvi dizer que vocês podem fazer um sistema para a gente que mostra a lista com todos nossos produtos, e nos deixa alterar um produto por outro.

Além disso, estamos pensando em ampliar nosso armazém, para ter mais espaço para mais produtos. Então, se puderem fazer com que o sistema nos permita adicionar mais produtos à lista, e qualquer outra coisa que acharem necessário, seria muito bom.

Desde já, agradeço!
'''

product_list: list[str] = []

def add_product(product, products):
  products.append(product)
  print("Produto {} adicionado à lista de produtos.".format(product))
# end def

def remove_product(product, products):
  if product in products:
    products.remove(product)
    print("Produto {} removido com sucesso.".format(product))
  else:
    print("Produto {} não existe na lista de produtos.".format(product))
#end def

def replace_product(orig_product, new_product, products):
  if orig_product in products:
    index = products.index(orig_product)
    products[index] = new_product
    print("O produto {} foi substituído pelo produto: {}.".format(orig_product, new_product))
  else:
    print("Esse produto com nome: {} não existe em nosso registro.".format(orig_product))
#end def

def showProducts(products):
  if (len(products) == 0):
    print("A lista de produtos está vazia!")
    return

  print("A lista de produtos solicitada possui os seguintes produtos:")
  for product in products:
    print(product)
# end def

add_product("Tomate", product_list)
showProducts(product_list)

replace_product("Tomate", "Gengibre", product_list)

remove_product("Tomate", product_list)
showProducts(product_list)
