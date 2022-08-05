from datetime import datetime, timedelta
from data import DataBr
from endereco import BuscaEndereco

cep = 95059050

obj_cep = BuscaEndereco(cep)

bairro, cidade, uf = obj_cep.acessa_via_cep()

print(bairro, cidade, uf)

# import requests

# r = requests.get('https://viacep.com.br/ws/95059050/json/')


# print(r.url)  # https://viacep.com.br/ws/95059050/json/
# print(r.status_code)  # 200
# print(r.request)  # <PreparedRequest [GET]>
# print(r.reason)  # ok
# print(r.raise_for_status())  # <bound method Response.raise_for_status of <Response [200]>>
# print(r.ok)  # True
# print(r.next)  # None
# print(r.links)  # {}
# print(r.json())  # <bound method Response.json of <Response [200]>>
# print(r.iter_lines())  # <bound method Response.iter_lines of <Response [200]>>
# print(r.iter_content())  # <bound method Response.iter_content of <Response [200]>>
# print(r.is_redirect)  # False
# print(r.is_permanent_redirect)  # False
# print(r.history)  # []
# print(r.encoding)  # utf-8
# print(r.elapsed)  # 0:00:00.560331
# print(r.cookies)  # <RequestsCookieJar[]>
# print(r.content)
# """
# b'{\n  "cep": "95059-050",\n  "logradouro": "Rua Apar\xc3\xadcio Borghetti",\n  "complemento": "",\n  "bairro": "S\xc3\xa3o 
# Crist\xc3\xb3v\xc3\xa3o",\n  "localidade": "Caxias do Sul",\n  "uf": "RS",\n  "ibge": "4305108",\n  "gia": "",\n  "ddd": "54",\n  "siafi": "8599"\n}'
# """
# print(r.connection)  # <requests.adapters.HTTPAdapter object at 0x000002546F286FA0>
# print(r.close)  # <bound method Response.close of <Response [200]>>
# print(r.apparent_encoding)  # utf-8

# print(r.headers)
"""
{
    'Server': 'nginx/1.22.0', 
    'Date': 'Fri, 05 Aug 2022 00:27:30 GMT', 
    'Content-Type': 'application/json; charset=utf-8', 
    'Transfer-Encoding': 'chunked', 
    'Connection': 'keep-alive', 
    'Expires': 'Fri, 05 Aug 2022 01:27:30 GMT', 
    'Cache-Control': 'max-age=3600, public', 
    'Pragma': 'public', 
    'Access-Control-Allow-Origin': '*', 
    'Access-Control-Allow-Methods': 'GET', 
    'Access-Control-Allow-Headers': 'Content-Type, X-Request-With, X-Requested-By', 
    'Access-Control-Allow-Credentials': 'true', 
    'Access-Control-Max-Age': '86400'}
"""


# print(dir(r))
"""
['__attrs__', '__bool__', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__enter__', '__eq__', '__exit__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__nonzero__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__setstate__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_content', '_content_consumed', '_next', 
'apparent_encoding', 'close', 'connection', 'content', 'cookies', 'elapsed', 'encoding', 'headers', 'history', 'is_permanent_redirect', 'is_redirect', 'iter_content', 'iter_lines', 'json', 'links', 'next', 'ok', 'raise_for_status', 'raw', 'reason', 'request', 'status_code', 'text', 'url']
"""

# hoje = datetime.today()
# amanha= datetime.today() + timedelta(days=1)

# print(hoje)  # 022-08-04 07:20:03.342771
# print(hoje - amanha)  # -1 day, 0:00:00

# cadastro = DataBr()
# print(type(cadastro.momento_cadastro))  # <class 'datetime.datetime'>
# print(cadastro)  # 04/08/2022 08:18
# print(cadastro.dia_semana())  # quinta
# print(cadastro.tempo_cadastro()) # 0:00:00.000999

# from telefone import TelefonesBr
# import re

# telefone = "552126481234"
# telefone_objeto = TelefonesBr(telefone)

#padrao = "([0-9]{2,3})?([0-9]{2})([0-9]{4,5})([0-9]{4})"
#resposta = re.search(padrao,telefone)
#print(resposta.group())

# print(telefone_objeto)


# import re

# padrao = '[0-9][a-z][0-9]'
# texto = "123 1a2 1cc aa1"
# resposta = re.search(padrao, texto)
# print(resposta)  # <re.Match object; span=(4, 7), match='1a2'>
# print(resposta.group())  # 1a2


# padrao = '[0-9][a-z]{2}[0-9]'
# texto = "123 1aj2 1cc aa1"
# resposta = re.search(padrao, texto)
# print(resposta)  # <re.Match object; span=(4, 8), match='1aj2'>
# print(resposta.group())  # 1aj2


# padrao = "\w{5,50}@\w{3,10}.\w{2,3}.\w{2,3}"
# texto = "aaabbbcc rodrigo123@gmail.com.br"
# resposta = re.search(padrao, texto)
# print(resposta)  # <re.Match object; span=(9, 32), match='rodrigo123@gmail.com.br'>
# print(resposta.group())  # rodrigo123@gmail.com.br

# from Documento import Documento

# cpf = 83469656053
# cnpj = 32757142000194
# # obj_cpf = Cpf(cpf)

# # print(obj_cpf)

# documento = Documento.cria_documento(cnpj)

# print(documento)