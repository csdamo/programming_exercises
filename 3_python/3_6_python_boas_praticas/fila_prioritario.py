from fila_base import FilaBase
from constantes import CODIGO_PRIORITARIO


class FilaPrioridade(FilaBase):

    def gera_senha_atual(self) -> None:
        self.senha_atual = f'{CODIGO_PRIORITARIO} {self.codigo}'

    def chama_cliente(self, caixa: int) -> str:
        cliente_atual: str = self.fila.pop(0)
        self.clientes_atendidos.append(cliente_atual)
        return f'Cliente atual: {cliente_atual} - Caixa: {caixa}'

    def estatistica(self, dia: str, agencia: int, flag: str) -> dict:
        if flag != 'detail':
            estatistica = {f'{agencia} - {dia}': len(self.clientes_atendidos)}
        else:
            estatistica = {
                'dia': dia,
                'agencia': agencia,
                'estatistica': self.clientes_atendidos,
                'quantidade': len(self.clientes_atendidos)
            }
        return estatistica
