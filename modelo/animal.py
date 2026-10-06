from clinica_veterinaria.modelo.entidade import Entidade


class Animal(Entidade):

    def __init__(self, id_entidade=0, nome="", especie="", raca="", idade=0, tutor=None):
        super().__init__(id_entidade)
        self._nome = nome
        self._especie = especie
        self._raca = raca
        self._idade = idade
        self._tutor = tutor

    def obter_nome(self):
        return self._nome

    def definir_nome(self, nome):
        self._nome = nome

    def obter_especie(self):
        return self._especie

    def definir_especie(self, especie):
        self._especie = especie

    def obter_raca(self):
        return self._raca

    def definir_raca(self, raca):
        self._raca = raca

    def obter_idade(self):
        return self._idade

    def definir_idade(self, idade):
        self._idade = idade

    def obter_tutor(self):
        return self._tutor

    def definir_tutor(self, tutor):
        self._tutor = tutor

    def tipo(self):
        return "Animal"

    def __str__(self):
        nome_tutor = self._tutor.obter_nome() if self._tutor else "nenhum"
        return (
            f"{super().__str__()} | nome={self._nome} | especie={self._especie} | "
            f"raca={self._raca} | idade={self._idade} | tutor={nome_tutor}"
        )
