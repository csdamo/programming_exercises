from typing import Union

from constantes import TIPO_FILA_NORMAL, TIPO_FILA_PRIORITARIA
from fila_normal import FilaNormal
from fila_prioritario import FilaPrioridade


class FabricaFila:
    @staticmethod
    def pega_fila(tipo_fila) -> Union[FilaNormal, FilaPrioridade]:
        if tipo_fila == TIPO_FILA_NORMAL:
            return FilaNormal()
        elif tipo_fila == TIPO_FILA_PRIORITARIA:
            return FilaPrioridade()
        else:
            raise NotImplementedError('Tipo de fila não existe')
