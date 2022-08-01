caminho = r'C:\Users\crist\desenv\1_programacao\3_python\3_4_python_IO\dados'
arquivo = caminho + '\contatos.csv'


# Abre o arquivo, se o método não é informado, usa o default 'read'
arquivo_contatos = open(arquivo, encoding='latin_1')  


# Le uma linha até encontrar a quebra de linha
conteudo = arquivo_contatos.readline()  # Le uma linha por vez
print('L1', conteudo)
conteudo = arquivo_contatos.readline()
print('L2', conteudo)


# se informado parâmetro, le até a posição indicada
conteudo = arquivo_contatos.readline(10)  
print('L3_0-10', conteudo)
conteudo = arquivo_contatos.readline() # começará a leitura de onde parou até encotrar a quebra de linha
print('L3_10-fim da linha', conteudo)


# readlines(): lê o arquivo inteiro
conteudo = arquivo_contatos.readlines()  
for linha in conteudo:
    print(linha, end='')
    
    
# com o for loop mostra todas as linhas,porém le uma linha de cada vez (método mais eficiente do que o readlines())
for linha in arquivo_contatos:  
    print(linha, end='')


