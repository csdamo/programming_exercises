from fabrica_fila import FabricaFila
from estatistica_detalhada import EstatisticaDetalhada
# from estatistica_resumida import EstatisticaResumida
# from fila_normal import FilaNormal
# from fila_prioritario import FilaPrioridade

fila_teste = FabricaFila.pega_fila('prioritaria')
fila_teste.atualiza_fila()
fila_teste.atualiza_fila()
fila_teste.atualiza_fila()
fila_teste.atualiza_fila()
print(fila_teste.chama_cliente(1))
print(fila_teste.chama_cliente(3))

print(fila_teste.estatistica(EstatisticaDetalhada('20/03/2025', 120)))

# print(fila_teste.estatistica('10/10/2022', 198, 'detail'))
