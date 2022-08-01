caminho = r'C:\Users\crist\desenv\1_programacao\3_python\3_4_python_IO\dados'
arquivo = caminho + '\contatos_escrita.csv'

contato1 = '11,Carol,carol@carol.com.br\n'
contato2 = '12,Andrezza,andrezza@andrezza.com.br\n'

with open(arquivo, encoding='latin_1', mode='w') as arquivo1:  
    arquivo1.write(contato1)

with open(arquivo, encoding='latin_1', mode='a') as arquivo2: 
    arquivo2.write(contato2)

