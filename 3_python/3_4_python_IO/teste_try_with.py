caminho = r'C:\Users\crist\desenv\1_programacao\3_python\3_4_python_IO\dados'
arquivo = caminho + '\contatos.csv'


try:
    with open(arquivo, encoding='latin_1') as arquivo_contatos: 
        for linha in arquivo_contatos:  
            print(linha, end='')
except FileNotFoundError:
    print('Arquivo não encontrado')
except PermissionError:
    print('Sem permissão para esctita')
    

