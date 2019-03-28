#!/usr/bin/env python
# coding: utf-8

# # <font color='blue'>Data Science Academy - Python Fundamentos - Capítulo 2</font>
# 
# ## Download: http://github.com/dsacademybr

# ## Exercícios Cap02

# In[2]:


# Exercício 1 - Imprima na tela os números de 1 a 10. Use uma lista para armazenar os números.
lista1 = [1,2,3,4,5,6,7,8,9,10]
print(lista1)


# In[3]:


# Exercício 2 - Crie uma lista de 5 objetos e imprima na tela
lista_animal = ['cachorro','cavalo','pato','ganso']
print(lista_animal)


# In[6]:


# Exercício 3 - Crie duas strings e concatene as duas em uma terceira string
frase1 ='Enquanto houver '
frase2 = 'amor, haverá esperança.'
frase3 = frase1 + frase2  
print(frase3)


# In[11]:


# Exercício 4 - Crie uma tupla com os seguintes elementos: 1, 2, 2, 3, 4, 4, 4, 5 e depois utilize a função count do 
# objeto tupla para verificar quantas vezes o número 4 aparece na tupla
tupla1 = (1, 2, 2, 3, 4, 4, 4, 5)
print(tupla1)
tupla1.count (4)


# In[12]:


# Exercício 5 - Crie um dicionário vazio e imprima na tela
dic_vazio = {}
print(dic_vazio)


# In[15]:


# Exercício 6 - Crie um dicionário com 3 chaves e 3 valores e imprima na tela
dic_chaves = {'Ana' : '35', 'Beatriz' : '38', 'Andre' : '45', 'Ricardo' : '28'}
print(dic_chaves)


# In[16]:


# Exercício 7 - Adicione mais um elemento ao dicionário criado no exercício anterior e imprima na tela
dic_chaves = {'Ana' : '35', 'Beatriz' : '38', 'Andre' : '45', 'Ricardo' : '28' , 'Gustavo' : '18'}
print(dic_chaves)


# In[18]:


# Exercício 8 - Crie um dicionário com 3 chaves e 3 valores. Um dos valores deve ser uma lista de 2 elementos numéricos. 
# Imprima o dicionário na tela.
dic_mescla = {'valor1' : '23', 'valor2' : '47', 'valor3': [23, 24, 33]}
print(dic_mescla)


# In[20]:


# Exercício 9 - Crie uma lista de 4 elementos. O primeiro elemento deve ser uma string, 
# o segundo uma tupla de 2 elementos, o terceiro um dcionário com 2 chaves e 2 valores e 
# o quarto elemento um valor do tipo float.
# Imprima a lista na tela.
lista_div = ['carambola',  (12, 340), {'amora' : '3', 'framboesa' : '27'}, 99.338]
print(lista_div)


# In[21]:


# Exercício 10 - Considere a string abaixo. Imprima na tela apenas os caracteres da posição 1 a 18.
frase = 'Cientista de Dados é o profissional mais sexy do século XXI'
frase[0:18]


# # Fim

# ### Obrigado - Data Science Academy - <a href="http://facebook.com/dsacademybr">facebook.com/dsacademybr</a>
