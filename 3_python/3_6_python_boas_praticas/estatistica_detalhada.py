from typing import List, Dict, Union


class EstatisticaDetalhada:
    def __init__(self, dia: str, agencia: int) -> None:
        self.dia = dia
        self.agencia = agencia

    def roda_estatistica(self, clientes_atendidos: List[str]) -> dict:
        estatistica: Dict[str, Union[List[str], str, int]] = {}
        estatistica['dia'] = self.dia
        estatistica['agencia'] = self.agencia
        estatistica['estatistica'] = clientes_atendidos
        estatistica['quantidade'] = len(clientes_atendidos)

        return estatistica
