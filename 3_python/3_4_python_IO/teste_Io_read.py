caminho = r'C:\Users\crist\desenv\1_programacao\3_python\3_4_python_IO\dados'
arquivo = caminho + '\contatos.csv'

arquivo_contato = open(arquivo, encoding='latin_1')

print(type(arquivo_contato))  # <class '_io.TextIOWrapper'>
print(type(arquivo_contato.buffer))  # <class '_io.BufferedReader'>

print(arquivo_contato.buffer) 
# <_io.BufferedReader name='C:\\Users\\crist\\desenv\\1_programacao\\3_python\\3_4_python_IO\\dados\\contatos.csv'>

print(arquivo_contato.buffer.read()) 
"""
    b'
    1,Guilherme,guilherme@guilherme.com.br\n
    2,Elias,elias@elias.com.br\n
    3,Gabriel,gabriel@gabriel.com.br\n
    4,Anderson,anderson@anderson.com.br\n
    5,Alex,alex@alex.com.br\n
    6,Vini,vini@vini.com.br\n
    7,Let\xedcia,leticia@leticia.com.br\n
    8,Giulia,giulia@giulia.com.br\n
    9,Felipe,felipe@felipe.com.br\n
    10,Lu\xedsa,luisa@luisa\n' 
"""

print(type(arquivo_contato.buffer.read()))  # <class 'bytes'>

text_bytes = bytes('Este é um texto em bytes', 'latin_1')  
print(text_bytes)  # b'Este \xe9 um texto em bytes'
print(type(text_bytes))  # <class 'bytes'>

arquivo_contato.close()