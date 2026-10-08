"""Liga os dados da tela às funções de terminal sem editar funcoes.py."""
import io
from unittest.mock import patch

import funcoes


def executar_funcao(funcao, *argumentos, respostas=()):
    """Fornece respostas prontas e captura as mensagens da função original.

    Usado somente em chamadas síncronas do Tkinter. A substituição temporária
    de input/print fica no módulo funcoes e é restaurada ao terminar.
    """
    entradas = iter(respostas)
    saida = io.StringIO()

    def ler(pergunta=""):
        try:
            return str(next(entradas))
        except StopIteration as erro:
            raise RuntimeError("As perguntas da função mudaram. Revise a integração.") from erro

    def imprimir(*valores, **opcoes):
        opcoes["file"] = saida
        print(*valores, **opcoes)

    with patch.object(funcoes, "input", ler, create=True), \
            patch.object(funcoes, "print", imprimir, create=True):
        resultado = funcao(*argumentos)
    return resultado, saida.getvalue().strip()
