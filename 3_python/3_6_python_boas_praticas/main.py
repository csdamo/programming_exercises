from fila_normal import FilaNormal
from fila_prioritario import FilaPrioridade

fila_teste = FilaPrioridade()
fila_teste1 = FilaNormal()
fila_teste.atualiza_fila()
fila_teste.atualiza_fila()
fila_teste.atualiza_fila()
fila_teste.atualiza_fila()
print(fila_teste.chama_cliente(1))
print(fila_teste.chama_cliente(3))

print(fila_teste.estatistica('10/10/2022', 198, 'detail'))
