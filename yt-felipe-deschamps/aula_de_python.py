# -*- coding: utf-8 -*-

#variáveis
nome = "michael"
#print(nome)
idade = 17
#print(idade)

#função que soma +1 a idade declarada
def mais_um_ano(idade) :
  print('ta dentro dessa função')
  return idade + 1;

#print(mais_um_ano(14))

#forma errada de armazenar vários valores que vão ser utilizados da mesma forma
filme1 = 'Toy Story 17'
filme2 = 'A xuxa contra o baixo astral'
filme3 = 'Matrix'
filmesTeste = [filme1,filme2,filme3]
#print(filmesTeste)

#forma correta de armazenar vários valores
filmes = ["Toy Story 17", 'A xuxa contra o baixo astral', 'Matrix']
#print(filmes)

#tipo de lista que é igual ao array no javascript
list()
#print(list)

''' def imprime_filmes(filmes_que_quero_imprimir) : 
  print('A lista de filmes que eu tenho disponível')
  print(filmes_que_quero_imprimir) '''

#pega a lista em geral que foi chamada
#print(imprime_filmes(filmes))

#pega o item da lista pelo seu respectivo index
#print(imprime_filmes(filmes[1]))

#pega o item da lista de trás para frente, no exemplo abaixo ele pega o ultimo filme
#print(imprime_filmes(filmes[-1]))

#pega o item da lista e mostra os itens que estão a frente dele
#print(imprime_filmes(filmes[-2:]))

#para cada item dentro da lista irá ser feito respectiva função
''' for filme in filmes :
  print(filme)
  print('...')
print('estou fora!') '''


#função que contém um for dentro dele 
def imprime_filmes(filmes_que_quero_imprimir) : 
  print('A lista de filmes que eu tenho disponível')
  for filme in filmes_que_quero_imprimir:
    print(filme)
    
#print(imprime_filmes(filmes))

dados = {
  "nome": "Guilherme", 
  "idade": 37, 
  "empresa": "Alura"
  }

print(dados["empresa"])