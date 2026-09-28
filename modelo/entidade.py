from abc import ABC, abstractmethod


class Entidade(ABC):
 

    def __init__(self, id_entidade=0):
        # Python nao tem "sobrecarga" de construtor (nao da pra ter um
        # Entidade() e um Entidade(id) ao mesmo tempo, como em Java).
        # O jeito de simular isso e dar um valor padrao ao parametro:
        # Entidade()  -> usa id_entidade=0 (o "construtor vazio")
        # Entidade(5) -> usa id_entidade=5 (o "construtor com id")
        self._id = id_entidade

    def obter_id(self):
        return self._id

    def definir_id(self, id_entidade):
        self._id = id_entidade

    @abstractmethod
    def tipo(self):
        """ Cada subclasse diz qual é o seu 'nome' """
        pass

    def __str__(self):
        return f"{self.tipo()} #{self._id}"
