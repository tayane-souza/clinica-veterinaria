from clinica_veterinaria.modelo.entidade import Entidade


class Procedimento(Entidade):

    def __init__(self, id_entidade=0, nome="", descricao="", valor_base=0.0, veterinario_responsavel=None):
        super().__init__(id_entidade)
        self._nome = nome
        self._descricao = descricao
        self._valor_base = valor_base
        self._veterinario_responsavel = veterinario_responsavel

    def obter_nome(self):
        return self._nome

    def definir_nome(self, nome):
        self._nome = nome

    def obter_descricao(self):
        return self._descricao

    def definir_descricao(self, descricao):
        self._descricao = descricao

    def obter_valor_base(self):
        return self._valor_base

    def definir_valor_base(self, valor_base):
        self._valor_base = valor_base

    def obter_veterinario_responsavel(self):
        return self._veterinario_responsavel

    def definir_veterinario_responsavel(self, veterinario):
        self._veterinario_responsavel = veterinario

    def tipo(self):
        return "Procedimento"

    def __str__(self):
        nome_vet = self._veterinario_responsavel.obter_nome() if self._veterinario_responsavel else "nenhum"
        return (
            f"{super().__str__()} | nome={self._nome} | descricao={self._descricao} | "
            f"valor_base={self._valor_base} | veterinario_responsavel={nome_vet}"
        )
