import contato_utils

caminho = r'C:\Users\crist\desenv\1_programacao\3_python\3_4_python_IO\dados'
arquivo = caminho + '\contatos.csv'


try:
    # contatos = contato_utils.csv_para_contatos(arquivo)
    # contato_utils.contatos_para_pickle(contatos, caminho + '/contato.pickle')
    # contatos = contato_utils.pickle_para_contato(caminho + '/contato.pickle')
    
    # contato_utils.contatos_para_json(contatos, caminho + '/contato.json')
    contatos = contato_utils.json_para_contato(caminho + '/contato.json')

    
    
    for contato in contatos:
        print(f'{contato.id} - {contato.nome} = {contato.email}')
        
except FileNotFoundError:
    print('Arquivo não encontrado')
except PermissionError:
    print('Sem permissão para esctita')

