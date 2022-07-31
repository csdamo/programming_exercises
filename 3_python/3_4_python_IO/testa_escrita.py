caminho = r'C:\Users\crist\desenv\1_programacao\3_python\3_4_python_IO\dados'
arquivo = caminho + '\contatos_escrita.csv'

# Abre o arquivo no mode de esccrita  # 'w' sobreescreve o contéudo já existente
arquivo_contatos = open(arquivo, encoding='latin_1', mode='w')  

contatos = [
    '11,Carol,carol@carol.com.br\n',
    '12,Ana,ana@ana.com.br\n',
    '13,Taís,tais@tais.com.br\n',
    '14,Felipe,felipe@felipe\n',
]

for contato in contatos:
    arquivo_contatos.write(contato)  # com o for, será escrita uma linha por vez

# apenas após fechar o arquivo será escrito as linhas, mas o método flush força a escrita antes do arquivo ser encerrado
arquivo_contatos.flush()  

# Se o método flush não or chamado, ocê perceberá que o arquivo será escrito somente depois de encerrar o programa
input('Precione <enter> para encerrar o programa')

# Abre o arquivo no mode de esccrita  # 'a' funciona como um append - não sobreescrevendo o conteúdo e incluindo o conteúdo no final do arquivo
arquivo_contatos = open(arquivo, encoding='latin_1', mode='a')  
contato = '11,Carol,carol@carol.com.br\n'

# Se o arquivo não existir, ele será criado e o conteúdo será escrito
arquivo_contatos.write(contato)