# Your task will be to generate the document term matrix, from documents retrieved from the internet and
# print this matrix to the screen. Therefore:
# a) Consider that all lists of sentences must be transformed into lists of vectors,
# where each item will be one of the words in the sentence.
# b) All vectors must be merged into a single corpus forming a list of vectors,
# where each item will be a lexeme.
# c) This single corpus will be used to generate the vocabulary.
# d) The expected result will be a term document matrix created from the application of the
# bag of words technique throughout the corpus.

import re
import pandas
import requests
from bs4 import BeautifulSoup

palavras = [] #Para armazenar as sentenças em cinco listas diferentes.
unicos = [] #Para armazenar as sentenças em cinco listas diferentes.
vetor = [] #Aqui é para verificar o numero de vezes que uma palavra aparece em um #determinado arquivo

#urls:
urls = ['https://www.ibm.com/cloud/learn/natural-language-processing', 
        'https://en.wikipedia.org/wiki/Natural_language_processing', 
        'https://monkeylearn.com/natural-language-processing/',
        'https://www.cio.com/article/228501/natural-language-processing-nlp-explained.html',
        'https://magnimindacademy.com/blog/how-do-natural-language-processing-systems-work/']

for site in urls:
    url = requests.get(site).content#guardar o conteudo do site
    soup = BeautifulSoup(url, "html.parser")
    for data in soup(['style', 'script']):#remover os scripts e estilos
        data.decompose()#remover os scripts e estilos
    palavra = ' '.join(soup.stripped_strings)
    palavra = re.sub(r"[\n\t]", "", palavra)#remover os espaços em branco
    separadores = re.split("[!?.;:,]", palavra)#separar as sentenças
    palavras.append(" ".join(separadores))#adicionar as sentenças em uma lista

def unico(p): #verificar se a palavra já existe no vetor
  sem_rep = set() #criar um conjunto vazio
  for array in p: #percorrer o vetor
    for palavra in array.split(): #percorrer cada palavra do vetor
        sem_rep.add(palavra) #adicionar a palavra no conjunto
  return sem_rep #retornar o conjunto

unicos = unico(palavras) #chamar a função unico
unicos = list(unicos) #transformar o conjunto em lista para poder usar o index
print(len(unicos)) #imprimir o tamanho do vetor

def BOW(arrayDePalavras, texto): #função para gerar a matriz termo documento
  array = [0] * len(arrayDePalavras)  #criar um vetor com o tamanho do vetor de palavras
  for string in texto.split(): #percorrer cada palavra do texto
    array[arrayDePalavras.index(string)] += 1 #adicionar 1 no vetor na posição da palavra
  return array #retornar o vetor

for array in palavras: #percorrer cada sentença
    vetor.append(BOW(unicos, array)) #chamar a função BOW e adicionar o vetor na lista

df = pandas.DataFrame(vetor, columns=unicos) #criar um dataframe com o vetor e as palavras
display(df) #imprimir o dataframe
