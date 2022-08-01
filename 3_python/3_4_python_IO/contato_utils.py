import csv, pickle, json
from contato import Contato

def csv_para_contatos(caminho, encoding='latin_1'):
    contatos = []
    
    with open(caminho, encoding=encoding) as arquivo:
        leitor = csv.reader(arquivo)
        
        for linha in leitor:
            
            id, nome, email= linha  # desempacotamento
            
            contato = contato = Contato(id, nome, email)
            
            # contato = Contato(
            #     id=linha[0],
            #     nome=linha[1],
            #     email=linha[2]
            # )
            contatos.append(contato)
    
    return contatos


def contatos_para_pickle(contatos, caminho):
    with open(caminho, mode='wb') as arquivo:
        pickle.dump(contatos, arquivo)
        
        
def pickle_para_contato(caminho):
    with open(caminho, mode='rb') as arquivo:
        contatos = pickle.load(arquivo)
        
    return contatos


def contatos_para_json(contatos, caminho):
    with open(caminho, mode='w') as arquivo:
        json.dump(contatos, arquivo, default=_contato_para_json)
        
        # a função '_contato_para_json' poderia ser substituida por uma função sem nome (lambda)
        # json.dump(contatos, arquivo, default=lambda contato: contato.__dict__)

        
def _contato_para_json(contato):
    return contato.__dict__
    
    
def json_para_contato(caminho):
    with open(caminho) as arquivo:
        contatos_json = json.load(arquivo)
        contatos = []
        for contato in contatos_json:
            c = Contato(**contato)  # desempacota
            
            # c = Contato(
            #     contato['id'],
            #     contato['nome'],
            #     contato['email']
            # )
            contatos.append(c)
        
    return contatos