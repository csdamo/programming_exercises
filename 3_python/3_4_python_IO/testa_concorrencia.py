caminho = r'C:\Users\crist\desenv\1_programacao\3_python\3_4_python_IO\dados'
arquivo = caminho + '\contatos_escrita.csv'

arquivo1 = open(arquivo, encoding='latin_1', mode='w')  
arquivo2 = open(arquivo, encoding='latin_1', mode='a')  

contato1 = '11,Carol,carol@carol.com.br\n'
contato2 = '12,Andrezza,andrezza@andrezza.com.br\n'

arquivo1.write(contato1)
arquivo2.write(contato2)

arquivo1.close()  # o fechamento é importante para liberar o recurso que está sendo utilizado
arquivo2.close()

# neste caso, as duas linhas serão escritas pois o segundo método (no 'arquivo2') é o 'a' 
# caso o método fosse 'w', a primeira linha seria sobreescrita
