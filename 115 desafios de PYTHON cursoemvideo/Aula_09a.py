#classes de manipulção de cadeia de texto
#1 - Fatiamento, Análise, Traformação, Divisão e junção
print('exemplos de manipulação de texto')
frase = 'Curso em Video Python'
print(frase[15])#fatiamento simples
print(frase[4:11])#fatiamento de trecho
print(len(frase))#mostra o comprimento da cadeia de texto
print(frase.count('o', 0, 20))#mostra quantas vezes aparece determinado trecho
print(frase.find('deo'))#find(encontrar) mostra onde começa um trecho de cadeia de string
print(frase.find('android'))#Essa cadeia não existe, portanto sempre retornará -1
print('Curso'in frase)#(in) é um operador porém pode ser usado para análise
print(frase.replace('Curso', 'Python'))# (replace: trocar ou reposicionar)troca um trecho da cadeia por outro definido
print(frase.upper())#transforma a cadeia, colocando-a em Maiúsculas(obrigatorio os parênteses)
print(frase.lower())#Faz o contrário do metódo upper
print(frase.capitalize())#tranforma toda a cadeia de texto em minúscula com exceção da primeira Letra
print(frase.title())#separa por palavras e capitaliza cada uma
frase = '   Aprenda Python  '
print(frase.strip())#strip retira os espaços excedentes do começo e fim da cadeia
print(frase.rstrip())#tira espaços do final apenas
print(frase.lstrip())#tira espaços do começo apenas
frase = 'Curso em Video Python'
print(frase.split())#forma padrão de split(divisão) tecnicamente faz uma lista de palavras da cadeia de texto
