caminho = r'C:\Users\crist\desenv\1_programacao\3_python\3_4_python_IO\dados'
arquivo = caminho + '\contatos_escrita.csv'

arquivo_contato = open(arquivo, encoding='latin_1', mode='a')

print(type(arquivo_contato.buffer))  
# 'w'ou 'a' <class '_io.BufferedWriter'>
# 'w+' ou 'a+' <class '_io.BufferedRandom'>

text_bytes = bytes('Este é um texto em bytes', 'latin_1')  

contato = bytes('15,Verônica,veronica@veronica.com.br\n', 'latin_1')

arquivo_contato.buffer.write(contato)

arquivo_contato.close()