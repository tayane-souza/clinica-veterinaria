from clinica_veterinaria.modelo.entidade import Entidade


class Consulta(Entidade):


    def __init__(self, id_entidade=0, data_consulta="", diagnostico="", animal=None, veterinario=None):
        super().__init__(id_entidade)
        self._data_consulta = data_consulta
        self._diagnostico = diagnostico
        self._animal = animal
        self._veterinario = veterinario
        self._itens = []

    def obter_data_consulta(self):
        return self._data_consulta

    def definir_data_consulta(self, data_consulta):
        self._data_consulta = data_consulta

    def obter_diagnostico(self):
        return self._diagnostico

    def definir_diagnostico(self, diagnostico):
        self._diagnostico = diagnostico

    def obter_animal(self):
        return self._animal

    def definir_animal(self, animal):
        self._animal = animal

    def obter_veterinario(self):
        return self._veterinario

    def definir_veterinario(self, veterinario):
        self._veterinario = veterinario

    def obter_itens(self):
        return self._itens

    def adicionar_item(self, item):
        self._itens.append(item)

    def remover_item(self, id_procedimento):
        for item in self._itens:
            if item.obter_procedimento().obter_id() == id_procedimento:
                self._itens.remove(item)
                return True
        return False

    def tipo(self):
        return "Consulta"

    def __str__(self):
        if self._itens:
            procedimentos = ", ".join(str(item) for item in self._itens)
        else:
            procedimentos = "nenhum procedimento"
        nome_animal = self._animal.obter_nome() if self._animal else "sem animal"
        nome_vet = self._veterinario.obter_nome() if self._veterinario else "sem veterinario"
        return (
            f"{super().__str__()} | data={self._data_consulta} | diagnostico={self._diagnostico} | "
            f"animal={nome_animal} | veterinario={nome_vet} | procedimentos=[{procedimentos}]"
        )
