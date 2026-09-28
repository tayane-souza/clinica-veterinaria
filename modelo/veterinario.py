from clinica_veterinaria.modelo.entidade import Entidade


class Veterinario(Entidade):

    def __init__(self, id_entidade=0, nome="", crmv="", especialidade="", coordenador=None):
        super().__init__(id_entidade)
        self._nome = nome
        self._crmv = crmv
        self._especialidade = especialidade
        self._coordenador = coordenador

    def obter_nome(self):
        return self._nome

    def definir_nome(self, nome):
        self._nome = nome

    def obter_crmv(self):
        return self._crmv

    def definir_crmv(self, crmv):
        self._crmv = crmv

    def obter_especialidade(self):
        return self._especialidade

    def definir_especialidade(self, especialidade):
        self._especialidade = especialidade

    def obter_coordenador(self):
        return self._coordenador

    def definir_coordenador(self, coordenador):
        self._coordenador = coordenador

    def tipo(self):
        return "Veterinario"

    def __str__(self):
        nome_coordenador = self._coordenador.obter_nome() if self._coordenador else "nenhum"
        return (
            f"{super().__str__()} | nome={self._nome} | crmv={self._crmv} | "
            f"especialidade={self._especialidade} | coordenador={nome_coordenador}"
        )
