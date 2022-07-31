caminho = r'C:\Users\crist\desenv\1_programacao\3_python\3_4_python_IO\dados'
arquivo = caminho + '\contatos_escrita.csv'

# Abre o arquivo no mode de esccrita e leitura
arquivo_contatos = open(arquivo, encoding='latin_1', mode='w+')  

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


# reposiciona o ponteiro para posição 28 (nesse, caso, segunda linha)
arquivo_contatos.seek(28)
# Sobrescrve a linha (para não sobreescrever usar o modo 'a' ou 'a+' - a nova linha será inserida no final do arquivo)
arquivo_contatos.write('12,Ana,ana@ana.com.br'.upper())


# reposiciona o ponteiro para posição 0 (inicio do arquivo)
arquivo_contatos.seek(0)

for linha in arquivo_contatos:
    print(linha, end='')