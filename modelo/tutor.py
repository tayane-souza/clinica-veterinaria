from clinica_veterinaria.modelo.entidade import Entidade


class Tutor(Entidade):

    def __init__(self, id_entidade=0, nome="", cpf="", telefone="", veterinario_responsavel=None):
        super().__init__(id_entidade)
        self._nome = nome
        self._cpf = cpf
        self._telefone = telefone
        self._veterinario_responsavel = veterinario_responsavel

    def obter_nome(self):
        return self._nome

    def definir_nome(self, nome):
        self._nome = nome

    def obter_cpf(self):
        return self._cpf

    def definir_cpf(self, cpf):
        self._cpf = cpf

    def obter_telefone(self):
        return self._telefone

    def definir_telefone(self, telefone):
        self._telefone = telefone

    def obter_veterinario_responsavel(self):
        return self._veterinario_responsavel

    def definir_veterinario_responsavel(self, veterinario):
        self._veterinario_responsavel = veterinario

    def tipo(self):
        return "Tutor"

    def __str__(self):
        nome_vet = self._veterinario_responsavel.obter_nome() if self._veterinario_responsavel else "nenhum"
        return (
            f"{super().__str__()} | nome={self._nome} | cpf={self._cpf} | "
            f"telefone={self._telefone} | veterinario_responsavel={nome_vet}"
        )
