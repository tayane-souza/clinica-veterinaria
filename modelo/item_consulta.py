class ItemConsulta:

    def __init__(self, procedimento, valor_cobrado=None):
        self._procedimento = procedimento
        self._valor_cobrado = valor_cobrado

    def obter_procedimento(self):
        return self._procedimento

    def definir_procedimento(self, procedimento):
        self._procedimento = procedimento

    def obter_valor_cobrado(self):
        return self._valor_cobrado

    def definir_valor_cobrado(self, valor_cobrado):
        self._valor_cobrado = valor_cobrado

    def __str__(self):
        valor = self._valor_cobrado if self._valor_cobrado is not None else self._procedimento.obter_valor_base()
        return f"{self._procedimento.obter_nome()} (valor cobrado: {valor})"
